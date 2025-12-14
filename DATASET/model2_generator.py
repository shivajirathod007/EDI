"""
Model-2 Dataset Generator - FINAL CLEAN VERSION
Save as: model2_generator.py
"""

import json
import random
import re
import uuid
from typing import Dict, List, Tuple
from tqdm import tqdm
from collections import Counter

# ============================================================
# CONFIGURATION
# ============================================================

MEMORY_TYPE_MAP = {
    "skill": "background",
    "device_requirement": "device_context",
    "constraint": "preference",
    "technical_skill": "background",
    "work_context": "project_context"
}

ALLOWED_MEMORY_TYPES = {
    "preference", "background", "project_context",
    "task_history", "device_context", "temporal_event"
}

INSTRUCTIONS = {
    "context_enrichment": [
        "Rewrite the prompt using only relevant memories. Do not add new facts.",
        "Enhance the prompt by incorporating applicable context only.",
        "Improve the prompt using relevant background while preserving intent.",
        "Integrate relevant memories to clarify the prompt without adding assumptions.",
        "Rewrite the user request using available relevant context."
    ],
    "semantic_anonymization": [
        "Remove or abstract personal identifiers while preserving intent.",
        "Anonymize sensitive entities without degrading task clarity.",
        "Rewrite the prompt to remove personal identifiers safely.",
        "Replace identifiable information with generic terms while maintaining meaning.",
        "Abstract personal details without losing the core request."
    ],
    "hybrid": [
        "Enrich the prompt using relevant memories and anonymize personal identifiers.",
        "Improve the prompt with useful context and remove any sensitive identifiers.",
        "Incorporate relevant background and ensure no personal information remains.",
        "Enhance with context while removing identifiable details.",
        "Add relevant context and anonymize sensitive information."
    ],
    "do_nothing": [
        "Evaluate memories for relevance. If none are relevant, return the original prompt unchanged.",
        "Only enrich if memories are clearly relevant to the task. Otherwise, preserve the original.",
        "Review available context. If not applicable, maintain the original prompt."
    ],
    "consent_blocked": [
        "Respect consent flags. Do not use memories if personalization is not allowed.",
        "Check user preferences. Only enrich if explicitly permitted by consent settings.",
        "Honor user consent. Return original prompt if personalization is disabled."
    ]
}

ENRICH_TEMPLATES = {
    "project_context": ["for work related to {}", "for a project involving {}", "in the context of {}"],
    "preference": ["with consideration for {}", "taking into account {}", "aligned with preference for {}"],
    "background": ["suitable for someone who {}", "appropriate for a user with {}", "optimized for someone with {}"],
    "device_context": ["that can handle {}", "capable of supporting {}", "designed for {}"],
    "task_history": ["based on recent activity involving {}", "considering past work with {}", "given previous experience with {}"],
    "temporal_event": ["given that {}", "considering that {}", "taking into account that {}"]
}

# ============================================================
# PII HANDLER (WITH WHITELIST)
# ============================================================

class PIIHandler:
    PII_REGEX = {
        "EMAIL": r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}\b',
        "PHONE": r'\b\d{10}\b|\b\d{3}[-.\s]?\d{3}[-.\s]?\d{4}\b',
        "PERSON_NAME": r'\b[A-Z][a-z]+ [A-Z][a-z]+\b',
        "CREDIT_CARD": r'\b\d{4}[\s-]?\d{4}[\s-]?\d{4}[\s-]?\d{4}\b'
    }
    
    NON_PII_WHITELIST = {
        "React Native", "Best Node", "Node JS", "React JS", "Spring Boot",
        "Machine Learning", "Deep Learning", "Data Science", "Big Data",
        "Apple Watch", "Google Drive", "Microsoft Office", "Amazon Prime",
        "Learn Spanish", "Learn Python", "Learn French", "Spanish Language",
        "Traditional Indian", "Italian Cuisine", "Chinese Food", "French Style",
        "Indian Cuisine", "Mexican Food", "Thai Cuisine", "Japanese Food",
        "Best Practices", "Quick Start", "Getting Started", "User Guide",
        "Data Analysis", "Web Development", "Mobile App", "Cloud Computing",
        "Project Manager", "Data Analyst", "Software Engineer", "Product Owner"
    }
    
    KNOWN_ENTITIES = {
        "PERSON": ["Alice", "Bob", "John", "Sarah", "Mike", "Emma", "Rahul", "Priya", "David", "Lisa", "Alice Smith", "John Doe", "Sarah Johnson", "Bob Wilson"],
        "ORG": ["TechCorp", "DataInc", "StartupXYZ", "GoogleInc", "Microsoft", "Amazon", "Meta"],
        "LOCATION": ["Mumbai", "Bangalore", "Pune", "Delhi", "San Francisco", "New York", "London", "Tokyo"]
    }
    
    SEMANTIC_REPLACEMENTS = {
        "EMAIL": "an email address",
        "PHONE": "a phone number",
        "PERSON_NAME": "a person",
        "PERSON": "a colleague",
        "ORG": "the organization",
        "LOCATION": "the location",
        "CREDIT_CARD": "a payment method"
    }
    
    @staticmethod
    def detect_pii(text: str) -> List[Tuple[str, str]]:
        found = []
        for pii_type, pattern in PIIHandler.PII_REGEX.items():
            for match in re.findall(pattern, text):
                if pii_type == "PERSON_NAME" and match in PIIHandler.NON_PII_WHITELIST:
                    continue
                found.append((pii_type, match))
        for entity_type, entities in PIIHandler.KNOWN_ENTITIES.items():
            for entity in entities:
                if entity in text:
                    found.append((entity_type, entity))
        return found
    
    @staticmethod
    def anonymize(text: str) -> Tuple[str, bool, str, List[str]]:
        pii_found = PIIHandler.detect_pii(text)
        if not pii_found:
            return text, False, "none", []
        anonymized = text
        removed = []
        for pii_type, pii_value in pii_found:
            replacement = PIIHandler.SEMANTIC_REPLACEMENTS.get(pii_type, "[redacted]")
            anonymized = anonymized.replace(pii_value, replacement)
            removed.append(f"{pii_type}:{pii_value}")
        strength = "high" if len(pii_found) >= 3 else "medium" if len(pii_found) >= 1 else "low"
        return anonymized, True, strength, removed

# ============================================================
# TRANSFORMATION ENGINE
# ============================================================

class TransformationEngine:
    @staticmethod
    def enrich(prompt: str, memories: List[Dict], max_context: int = 3) -> Tuple[str, List[str], str]:
        phrases = []
        used_ids = []
        relevant_memories = [m for m in memories if m["relevance"] == "high" and m.get("allowed_for_use", False)][:max_context]
        
        if not relevant_memories:
            return prompt, [], "none"
        
        for mem in relevant_memories:
            mem_type = mem["memory_type"]
            mem_text = mem["memory_text"].lower().strip()
            templates = ENRICH_TEMPLATES.get(mem_type, [])
            if templates:
                random.shuffle(templates)
                template = templates[0]
                phrases.append(template.format(mem_text))
                used_ids.append(mem["memory_id"])
        
        if not phrases:
            return prompt, [], "none"
        
        enriched = f"{prompt}, " + ", ".join(phrases)
        strength = "high" if len(used_ids) >= 2 else "medium" if len(used_ids) == 1 else "low"
        return enriched, used_ids, strength
    
    @staticmethod
    def anonymize(text: str) -> Tuple[str, bool, str, List[str]]:
        return PIIHandler.anonymize(text)
    
    @staticmethod
    def hybrid_transform(prompt: str, memories: List[Dict], consent_flags: Dict) -> Dict:
        result = {
            "enriched": prompt, "anonymized": prompt, "used_memories": [],
            "removed_pii": [], "enrichment_strength": "none",
            "anonymization_strength": "none", "transformation_order": []
        }
        
        if consent_flags.get("allow_personalization", False):
            enriched, used_ids, enrich_strength = TransformationEngine.enrich(prompt, memories)
            result["enriched"] = enriched
            result["used_memories"] = used_ids
            result["enrichment_strength"] = enrich_strength
            if enrich_strength != "none":
                result["transformation_order"].append("enrich")
        
        if consent_flags.get("allow_anonymization", False):
            base_text = result["enriched"]
            anonymized, had_pii, strength, pii_list = TransformationEngine.anonymize(base_text)
            result["anonymized"] = anonymized
            result["anonymization_strength"] = strength
            result["removed_pii"] = pii_list
            if strength != "none":
                result["transformation_order"].append("anonymize")
        
        if not result["transformation_order"]:
            result["transformation_order"] = ["none"]
        
        return result

# ============================================================
# SAMPLE GENERATOR
# ============================================================

class Model2SampleGenerator:
    def __init__(self, rules: List[Dict]):
        self.rules = rules
        self.transformer = TransformationEngine()
    
    def _normalize_mem_type(self, mem_type: str) -> str:
        normalized = MEMORY_TYPE_MAP.get(mem_type, mem_type)
        if normalized not in ALLOWED_MEMORY_TYPES:
            raise ValueError(f"Invalid memory_type: {mem_type}")
        return normalized
    
    def _build_memories(self, rule: Dict, high_count: int = 2, medium_count: int = 1, low_count: int = 2) -> List[Dict]:
        memories = []
        def add_memories(mem_list, relevance, count):
            available = min(count, len(mem_list))
            for mem_text, mem_type in random.sample(mem_list, available):
                memories.append({
                    "memory_id": f"mem_{uuid.uuid4().hex[:8]}",
                    "memory_text": mem_text,
                    "memory_type": self._normalize_mem_type(mem_type),
                    "relevance": relevance,
                    "source": "model1",
                    "allowed_for_use": True
                })
        add_memories(rule["highly_relevant"], "high", high_count)
        add_memories(rule.get("somewhat_relevant", []), "medium", medium_count)
        add_memories(rule["not_relevant"], "low", low_count)
        random.shuffle(memories)
        return memories
    
    def generate_enrichment(self) -> Dict:
        rule = random.choice(self.rules)
        prompt = random.choice(rule["prompts"])
        memories = self._build_memories(rule)
        enriched, used_ids, enrich_strength = self.transformer.enrich(prompt, memories)
        pii_in_output = len(PIIHandler.detect_pii(enriched)) > 0
        
        return {
            "id": str(uuid.uuid4()),
            "task_type": "context_enrichment",
            "instruction": random.choice(INSTRUCTIONS["context_enrichment"]),
            "raw_prompt": prompt,
            "retrieved_memories": memories,
            "user_consent_flags": {"allow_personalization": True, "allow_anonymization": False, "allow_sensitive_use": False},
            "constraints": {"max_tokens": 200, "tone": "neutral", "no_assumptions": True, "no_external_facts": True, "preserve_intent": True},
            "expected_output": enriched,
            "quality_tags": {
                "contains_pii": pii_in_output,
                "anonymization_strength": "none",
                "enrichment_strength": enrich_strength,
                "hallucination_risk": "low",
                "review_status": "rule_verified",
                "used_memories": used_ids,
                "removed_pii": [],
                "transformation_order": ["enrich"] if enrich_strength != "none" else ["none"],
                "category": rule["category"]
            }
        }
    
    def generate_anonymization(self) -> Dict:
        pii_templates = [
            "Alice Smith from TechCorp wants to discuss the project in Mumbai",
            "My email is john.doe@example.com and phone is 9876543210",
            "Meet Sarah Johnson at San Francisco office next week",
            "Contact Bob at bob.wilson@microsoft.com for the DataInc partnership",
            "Rahul from Bangalore mentioned his credit card 4532-1234-5678-9010",
            "Send the report to priya.sharma@techinc.com by Friday",
            "My manager John Smith suggested meeting at the Pune office",
            "Call me on 4155551234 to discuss the Mumbai project",
            "Alice will share her email alice.jones@startup.com tomorrow"
        ]
        prompt = random.choice(pii_templates)
        anonymized, had_pii, strength, pii_list = self.transformer.anonymize(prompt)
        pii_in_output = len(PIIHandler.detect_pii(anonymized)) > 0
        
        return {
            "id": str(uuid.uuid4()),
            "task_type": "semantic_anonymization",
            "instruction": random.choice(INSTRUCTIONS["semantic_anonymization"]),
            "raw_prompt": prompt,
            "retrieved_memories": [],
            "user_consent_flags": {"allow_personalization": False, "allow_anonymization": True, "allow_sensitive_use": False},
            "constraints": {"max_tokens": 200, "tone": "neutral", "no_assumptions": True, "no_external_facts": True, "preserve_intent": True},
            "expected_output": anonymized,
            "quality_tags": {
                "contains_pii": pii_in_output,
                "anonymization_strength": strength,
                "enrichment_strength": "none",
                "hallucination_risk": "low",
                "review_status": "rule_verified",
                "used_memories": [],
                "removed_pii": pii_list,
                "transformation_order": ["anonymize"] if strength != "none" else ["none"],
                "category": "privacy_preservation"
            }
        }
    
    def generate_hybrid(self) -> Dict:
        rule = random.choice(self.rules)
        base_prompts = rule["prompts"]
        pii_additions = [
            " for my work at TechCorp in Mumbai",
            " contact me at john.doe@example.com",
            " call me on 9876543210",
            " for Alice Smith's project",
            " email me at sarah.j@startup.com",
            " at the Bangalore office",
            " for work with Bob Wilson",
            " reach me on 4155551234"
        ]
        prompt = random.choice(base_prompts) + random.choice(pii_additions)
        memories = self._build_memories(rule)
        consent_flags = {"allow_personalization": True, "allow_anonymization": True, "allow_sensitive_use": False}
        result = self.transformer.hybrid_transform(prompt, memories, consent_flags)
        pii_in_output = len(PIIHandler.detect_pii(result["anonymized"])) > 0
        
        return {
            "id": str(uuid.uuid4()),
            "task_type": "hybrid",
            "instruction": random.choice(INSTRUCTIONS["hybrid"]),
            "raw_prompt": prompt,
            "retrieved_memories": memories,
            "user_consent_flags": consent_flags,
            "constraints": {"max_tokens": 200, "tone": "neutral", "no_assumptions": True, "no_external_facts": True, "preserve_intent": True},
            "expected_output": result["anonymized"],
            "quality_tags": {
                "contains_pii": pii_in_output,
                "anonymization_strength": result["anonymization_strength"],
                "enrichment_strength": result["enrichment_strength"],
                "hallucination_risk": "low",
                "review_status": "rule_verified",
                "used_memories": result["used_memories"],
                "removed_pii": result["removed_pii"],
                "transformation_order": result["transformation_order"],
                "category": rule["category"]
            }
        }
    
    def generate_do_nothing(self) -> Dict:
        rule = random.choice(self.rules)
        prompt = random.choice(rule["prompts"])
        memories = self._build_memories(rule, high_count=0, medium_count=0, low_count=4)
        
        return {
            "id": str(uuid.uuid4()),
            "task_type": "context_enrichment",
            "instruction": random.choice(INSTRUCTIONS["do_nothing"]),
            "raw_prompt": prompt,
            "retrieved_memories": memories,
            "user_consent_flags": {"allow_personalization": True, "allow_anonymization": False, "allow_sensitive_use": False},
            "constraints": {"max_tokens": 200, "tone": "neutral", "no_assumptions": True, "no_external_facts": True, "preserve_intent": True},
            "expected_output": prompt,
            "quality_tags": {
                "contains_pii": False,
                "anonymization_strength": "none",
                "enrichment_strength": "none",
                "hallucination_risk": "low",
                "review_status": "rule_verified",
                "used_memories": [],
                "removed_pii": [],
                "transformation_order": ["none"],
                "category": rule["category"],
                "special_case": "do_nothing"
            }
        }
    
    def generate_consent_blocked(self) -> Dict:
        rule = random.choice(self.rules)
        prompt = random.choice(rule["prompts"])
        memories = self._build_memories(rule, high_count=2, medium_count=1, low_count=1)
        for mem in memories:
            mem["allowed_for_use"] = False
        
        return {
            "id": str(uuid.uuid4()),
            "task_type": "context_enrichment",
            "instruction": random.choice(INSTRUCTIONS["consent_blocked"]),
            "raw_prompt": prompt,
            "retrieved_memories": memories,
            "user_consent_flags": {"allow_personalization": False, "allow_anonymization": False, "allow_sensitive_use": False},
            "constraints": {"max_tokens": 200, "tone": "neutral", "no_assumptions": True, "no_external_facts": True, "preserve_intent": True},
            "expected_output": prompt,
            "quality_tags": {
                "contains_pii": False,
                "anonymization_strength": "none",
                "enrichment_strength": "none",
                "hallucination_risk": "low",
                "review_status": "rule_verified",
                "used_memories": [],
                "removed_pii": [],
                "transformation_order": ["none"],
                "category": rule["category"],
                "special_case": "consent_blocked"
            }
        }

# ============================================================
# VALIDATOR
# ============================================================

class Validator:
    INTENT_MAP = {
        "laptop": {"laptop", "computer", "device", "machine", "system"},
        "travel": {"travel", "trip", "vacation", "journey", "visit"},
        "plan": {"plan", "planning", "organize", "schedule", "arrange"},
        "suggest": {"suggest", "recommend", "advise", "propose"},
        "help": {"help", "assist", "support", "guide"}
    }
    
    @staticmethod
    def validate(sample: Dict) -> Tuple[bool, List[str]]:
        issues = []
        pii_in_output = PIIHandler.detect_pii(sample["expected_output"])
        if pii_in_output:
            issues.append(f"PII leaked: {pii_in_output}")
        
        raw = sample["raw_prompt"].lower()
        output = sample["expected_output"].lower()
        intent_preserved = False
        for concept, terms in Validator.INTENT_MAP.items():
            if any(term in raw for term in terms):
                if any(term in output for term in terms):
                    intent_preserved = True
                    break
        
        if not intent_preserved:
            if sample.get("quality_tags", {}).get("special_case") in ["do_nothing", "consent_blocked"]:
                intent_preserved = True
            else:
                raw_words = set(raw.split())
                output_words = set(output.split())
                overlap = len(raw_words & output_words) / len(raw_words) if raw_words else 0
                if overlap < 0.3:
                    issues.append("Intent not preserved")
        
        if len(sample["expected_output"]) > 500:
            issues.append("Output too long")
        if not sample["expected_output"].strip():
            issues.append("Empty output")
        
        return len(issues) == 0, issues

# ============================================================
# MAIN GENERATION
# ============================================================

def generate_model2_dataset(rules: List[Dict], output_path: str = "model2_dataset.jsonl", target_size: int = 20000):
    print("="*70)
    print("🚀 Model-2 Dataset Generator (FINAL VERSION)")
    print("="*70)
    
    generator = Model2SampleGenerator(rules)
    validator = Validator()
    
    distribution = {
        "context_enrichment": int(target_size * 0.35),
        "semantic_anonymization": int(target_size * 0.30),
        "hybrid": int(target_size * 0.27),
        "do_nothing": int(target_size * 0.05),
        "consent_blocked": int(target_size * 0.03)
    }
    
    print(f"\n📊 Target: {target_size} samples")
    print(f"Distribution: {distribution}\n")
    
    stats = {"generated": 0, "valid": 0, "rejected": 0, "rejection_reasons": Counter(), "task_counts": Counter()}
    
    with open(output_path, "w", encoding="utf-8") as f:
        for task_type, count in distribution.items():
            print(f"📝 Generating {count} {task_type} samples...")
            task_valid = 0
            attempts = 0
            max_attempts = count * 3
            
            with tqdm(total=count, desc=f"{task_type}") as pbar:
                while task_valid < count and attempts < max_attempts:
                    attempts += 1
                    stats["generated"] += 1
                    
                    try:
                        if task_type == "context_enrichment":
                            sample = generator.generate_enrichment()
                        elif task_type == "semantic_anonymization":
                            sample = generator.generate_anonymization()
                        elif task_type == "hybrid":
                            sample = generator.generate_hybrid()
                        elif task_type == "do_nothing":
                            sample = generator.generate_do_nothing()
                        elif task_type == "consent_blocked":
                            sample = generator.generate_consent_blocked()
                        
                        is_valid, issues = validator.validate(sample)
                        
                        if is_valid:
                            f.write(json.dumps(sample) + "\n")
                            stats["valid"] += 1
                            stats["task_counts"][task_type] += 1
                            task_valid += 1
                            pbar.update(1)
                        else:
                            stats["rejected"] += 1
                            for issue in issues:
                                stats["rejection_reasons"][issue] += 1
                    
                    except Exception as e:
                        stats["rejected"] += 1
                        stats["rejection_reasons"][f"Exception: {str(e)}"] += 1
    
    print("\n" + "="*70)
    print("✅ GENERATION COMPLETE")
    print("="*70)
    print(f"Valid samples: {stats['valid']}")
    print(f"Rejected: {stats['rejected']}")
    print(f"Success rate: {stats['valid']/stats['generated']*100:.1f}%\n")
    print(f"💾 Output: {output_path}")
    print("="*70)
    return stats

# ============================================================
# MAIN
# ============================================================

if __name__ == "__main__":
    from prompt_memory_rules import PROMPT_MEMORY_RULES
    
    print("""
╔═══════════════════════════════════════════════════════════════════╗
║           Model-2 Dataset Generator (FINAL)                      ║
║           ✅ Fixed PII Detection                                 ║
║           ✅ Production Ready                                     ║
╚═══════════════════════════════════════════════════════════════════╝
""")
    
    size = input("Enter dataset size (default: 20000): ").strip()
    size = int(size) if size else 20000
    
    output = input("Enter output filename (default: model2_final_20k.jsonl): ").strip()
    output = output if output else "model2_final_20k.jsonl"
    
    print(f"\n🚀 Generating {size} samples...")
    print(f"📁 Output: {output}")
    print(f"⏱️  Estimated time: ~{size//500} minutes\n")
    
    stats = generate_model2_dataset(
        rules=PROMPT_MEMORY_RULES,
        output_path=output,
        target_size=size
    )
    
    print(f"\n✅ Done! Next steps:")
    print(f"   1. Quality check: python model2_quality_check.py {output}")
    print(f"   2. If pass rate > 99%, split for training")
    print(f"   3. Start Model-2 training")