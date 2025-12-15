# COMPREHENSIVE PROMPT-MEMORY RULES
# -----------------------------
PROMPT_MEMORY_RULES = [
    # ===== TECHNOLOGY & DEVELOPMENT (40 categories) =====
    {
        "category": "laptop_recommendations",
        "prompts": [
            "Suggest me a laptop for coding", "Which laptop should I buy for development?",
            "Recommend a good programming laptop", "Best laptop for software development?",
            "I need a new laptop for my CS work", "Help me choose a developer laptop"
        ],
        "highly_relevant": [
            ("Prefers AMD CPUs for development.", "preference"),
            ("Likes quiet laptop fans.", "preference"),
            ("Prefers high refresh-rate displays.", "preference"),
            ("Recently searched for laptop recommendations.", "task_history"),
            ("Three days ago discussed laptop performance.", "temporal_event"),
            ("Budget is around $1500 for electronics.", "preference")
        ],
        "somewhat_relevant": [
            ("Studies Computer Engineering.", "background"),
            ("Has experience in backend development.", "background"),
            ("Uses device mainly for coding 8+ hours daily.", "device_context"),
            ("Working on AWAF dashboard backend.", "project_context")
        ],
        "not_relevant": [
            ("Prefers vegetarian food.", "preference"),
            ("Last week searched for weekend trip ideas.", "temporal_event"),
            ("Enjoys morning jogs in the park.", "preference"),
            ("Visited Thailand last year.", "background")
        ]
    },
    {
        "category": "programming_language_learning",
        "prompts": [
            "Which programming language should I learn next?", "Suggest a new language to learn",
            "What coding language is best for my career?", "Recommend a programming language",
            "Should I learn Rust or Go?", "What language is trending now?"
        ],
        "highly_relevant": [
            ("Knows Python, C++, and Bash.", "background"),
            ("Enjoys Rust programming.", "preference"),
            ("Is learning AI model training techniques.", "background"),
            ("Asked about functional programming last month.", "temporal_event")
        ],
        "somewhat_relevant": [
            ("Has experience in backend development.", "background"),
            ("Studies Computer Engineering.", "background"),
            ("Working on AWAF dashboard backend.", "project_context"),
            ("Participates in research groups at college.", "background")
        ],
        "not_relevant": [
            ("Prefers vegetarian food.", "preference"),
            ("Usually free after 6 PM.", "device_context"),
            ("Enjoys hiking on weekends.", "preference")
        ]
    },
    {
        "category": "debugging_help",
        "prompts": [
            "Help me debug my code", "Why is my program crashing?",
            "Explain this error message", "How do I fix this bug?",
            "My code isn't working", "I'm getting a segmentation fault"
        ],
        "highly_relevant": [
            ("Completed a debugging task last night.", "task_history"),
            ("Yesterday asked about error logs.", "temporal_event"),
            ("Working on AWAF dashboard backend.", "project_context"),
            ("Recently encountered Python import errors.", "task_history")
        ],
        "somewhat_relevant": [
            ("Knows Python, C++, and Bash.", "background"),
            ("Has experience in backend development.", "background"),
            ("Uses VS Code with debugger extensions.", "preference")
        ],
        "not_relevant": [
            ("Prefers vegetarian food.", "preference"),
            ("Last week searched for weekend trip ideas.", "temporal_event"),
            ("Usually free after 6 PM.", "device_context")
        ]
    },
    {
        "category": "code_optimization",
        "prompts": [
            "How can I optimize my code?", "Make my program run faster",
            "Improve algorithm performance", "Reduce memory usage in my app",
            "My code is too slow", "Optimize database queries"
        ],
        "highly_relevant": [
            ("Optimizing vector search for hybrid AI.", "project_context"),
            ("Working on performance-critical backend services.", "project_context"),
            ("Recently profiled code for bottlenecks.", "task_history")
        ],
        "somewhat_relevant": [
            ("Has experience in backend development.", "background"),
            ("Knows Python, C++, and Bash.", "background"),
            ("Studies algorithms and data structures.", "background")
        ],
        "not_relevant": [
            ("Prefers vegetarian food.", "preference"),
            ("Enjoys photography in spare time.", "preference")
        ]
    },
    {
        "category": "project_suggestions",
        "prompts": [
            "Suggest improvements for my current project", "How can I enhance my project?",
            "Give feedback on my project", "What should I add to my app?",
            "Project ideas for my portfolio", "How to make my project stand out?"
        ],
        "highly_relevant": [
            ("Working on AWAF dashboard backend.", "project_context"),
            ("Training LSTM model for anomaly detection.", "project_context"),
            ("Building a police data platform in Node.js.", "project_context"),
            ("Recently reviewed project architecture.", "task_history")
        ],
        "somewhat_relevant": [
            ("Has experience in backend development.", "background"),
            ("Knows Python, C++, and Bash.", "background"),
            ("Participates in hackathons.", "background")
        ],
        "not_relevant": [
            ("Prefers vegetarian food.", "preference"),
            ("Usually free after 6 PM.", "device_context")
        ]
    },
    {
        "category": "framework_choice",
        "prompts": [
            "Should I use React or Vue?", "Which framework is better for my project?",
            "Django vs Flask comparison", "Best Node.js framework",
            "Recommend a web framework", "FastAPI or Express?"
        ],
        "highly_relevant": [
            ("Building a police data platform in Node.js.", "project_context"),
            ("Prefers lightweight frameworks.", "preference"),
            ("Recently compared backend frameworks.", "task_history")
        ],
        "somewhat_relevant": [
            ("Has experience in backend development.", "background"),
            ("Working on web dashboard.", "project_context")
        ],
        "not_relevant": [
            ("Prefers vegetarian food.", "preference"),
            ("Enjoys morning jogs.", "preference")
        ]
    },
    {
        "category": "api_development",
        "prompts": [
            "How to design a REST API?", "Best practices for API development",
            "Create GraphQL API", "API authentication methods",
            "Rate limiting for APIs", "API versioning strategies"
        ],
        "highly_relevant": [
            ("Working on AWAF dashboard backend.", "project_context"),
            ("Has experience in backend development.", "background"),
            ("Recently implemented JWT authentication.", "task_history")
        ],
        "somewhat_relevant": [
            ("Knows Python, C++, and Bash.", "background"),
            ("Building a police data platform in Node.js.", "project_context")
        ],
        "not_relevant": [
            ("Prefers vegetarian food.", "preference"),
            ("Last week searched for weekend trip ideas.", "temporal_event")
        ]
    },
    {
        "category": "database_selection",
        "prompts": [
            "Which database should I use?", "PostgreSQL vs MongoDB",
            "Best database for my app", "SQL or NoSQL?",
            "Database for high traffic app", "Redis for caching?"
        ],
        "highly_relevant": [
            ("Optimizing vector search for hybrid AI.", "project_context"),
            ("Working on data-intensive backend.", "project_context"),
            ("Recently evaluated database options.", "task_history")
        ],
        "somewhat_relevant": [
            ("Has experience in backend development.", "background"),
            ("Building a police data platform in Node.js.", "project_context")
        ],
        "not_relevant": [
            ("Prefers vegetarian food.", "preference"),
            ("Enjoys photography.", "preference")
        ]
    },
    {
        "category": "deployment_devops",
        "prompts": [
            "How to deploy my app?", "Docker vs Kubernetes",
            "CI/CD pipeline setup", "Deploy to AWS or Azure?",
            "Best hosting for my project", "Container orchestration help"
        ],
        "highly_relevant": [
            ("Recently configured deployment pipeline.", "task_history"),
            ("Working on production deployment.", "project_context"),
            ("Uses Docker for development.", "preference")
        ],
        "somewhat_relevant": [
            ("Has experience in backend development.", "background"),
            ("Knows Linux system administration.", "background")
        ],
        "not_relevant": [
            ("Prefers vegetarian food.", "preference"),
            ("Enjoys morning jogs.", "preference")
        ]
    },
    {
        "category": "testing_qa",
        "prompts": [
            "How to write unit tests?", "Testing best practices",
            "Jest vs Mocha for testing", "Integration testing guide",
            "TDD methodology help", "Mock API calls in tests"
        ],
        "highly_relevant": [
            ("Recently implemented test suite.", "task_history"),
            ("Working on improving code coverage.", "project_context"),
            ("Prefers test-driven development.", "preference")
        ],
        "somewhat_relevant": [
            ("Has experience in backend development.", "background"),
            ("Working on AWAF dashboard backend.", "project_context")
        ],
        "not_relevant": [
            ("Prefers vegetarian food.", "preference"),
            ("Last week searched for weekend trip ideas.", "temporal_event")
        ]
    },
    {
        "category": "version_control",
        "prompts": [
            "Git best practices", "How to resolve merge conflicts?",
            "Git branching strategy", "Rebase vs merge",
            "GitHub workflow help", "Git commands explanation"
        ],
        "highly_relevant": [
            ("Recently had merge conflict issues.", "task_history"),
            ("Uses Git for all projects.", "preference"),
            ("Collaborated on open source projects.", "background")
        ],
        "somewhat_relevant": [
            ("Has experience in backend development.", "background"),
            ("Working on team project.", "project_context")
        ],
        "not_relevant": [
            ("Prefers vegetarian food.", "preference"),
            ("Enjoys hiking.", "preference")
        ]
    },
    {
        "category": "security_practices",
        "prompts": [
            "How to secure my API?", "Prevent SQL injection",
            "Best security practices", "OWASP top 10 explained",
            "Encrypt sensitive data", "XSS protection methods"
        ],
        "highly_relevant": [
            ("Works on cybersecurity projects.", "background"),
            ("Completed a DDoS detection experiment.", "task_history"),
            ("Working on metadata-cleaner security project.", "project_context"),
            ("Configured firewall rules last week.", "temporal_event")
        ],
        "somewhat_relevant": [
            ("Has experience in backend development.", "background"),
            ("Studies network security.", "background")
        ],
        "not_relevant": [
            ("Prefers vegetarian food.", "preference"),
            ("Enjoys morning jogs.", "preference")
        ]
    },
    {
        "category": "ml_ai_basics",
        "prompts": [
            "How to start with machine learning?", "Explain neural networks",
            "ML algorithms overview", "Training my first model",
            "Deep learning tutorials", "AI project ideas"
        ],
        "highly_relevant": [
            ("Is learning AI model training techniques.", "background"),
            ("Training LSTM model for anomaly detection.", "project_context"),
            ("Recently studied ML fundamentals.", "task_history")
        ],
        "somewhat_relevant": [
            ("Knows Python programming.", "background"),
            ("Studies Computer Engineering.", "background")
        ],
        "not_relevant": [
            ("Prefers vegetarian food.", "preference"),
            ("Last week searched for weekend trip ideas.", "temporal_event")
        ]
    },
    {
        "category": "data_preprocessing",
        "prompts": [
            "How to clean my dataset?", "Data preprocessing techniques",
            "Handle missing values", "Feature engineering tips",
            "Normalize data for ML", "Deal with imbalanced data"
        ],
        "highly_relevant": [
            ("Training LSTM model for anomaly detection.", "project_context"),
            ("Recently worked on dataset cleaning.", "task_history"),
            ("Working with large datasets.", "project_context")
        ],
        "somewhat_relevant": [
            ("Is learning AI model training techniques.", "background"),
            ("Knows Python and pandas.", "background")
        ],
        "not_relevant": [
            ("Prefers vegetarian food.", "preference"),
            ("Enjoys photography.", "preference")
        ]
    },
    {
        "category": "model_training",
        "prompts": [
            "How to train ML model efficiently?", "Hyperparameter tuning guide",
            "Prevent overfitting", "Cross-validation explained",
            "Learning rate optimization", "Batch size selection"
        ],
        "highly_relevant": [
            ("Training LSTM model for anomaly detection.", "project_context"),
            ("Is learning AI model training techniques.", "background"),
            ("Recently experimented with model architectures.", "task_history")
        ],
        "somewhat_relevant": [
            ("Knows Python programming.", "background"),
            ("Has GPU for training.", "device_context")
        ],
        "not_relevant": [
            ("Prefers vegetarian food.", "preference"),
            ("Usually free after 6 PM.", "device_context")
        ]
    },
    {
        "category": "data_visualization",
        "prompts": [
            "How to visualize my data?", "Create interactive charts",
            "Matplotlib vs Plotly", "Dashboard design tips",
            "Best visualization library", "Plot time series data"
        ],
        "highly_relevant": [
            ("Working on AWAF dashboard backend.", "project_context"),
            ("Recently created data visualizations.", "task_history"),
            ("Prefers clean, minimal charts.", "preference")
        ],
        "somewhat_relevant": [
            ("Knows Python programming.", "background"),
            ("Working with datasets.", "project_context")
        ],
        "not_relevant": [
            ("Prefers vegetarian food.", "preference"),
            ("Enjoys hiking.", "preference")
        ]
    },
    {
        "category": "cloud_services",
        "prompts": [
            "AWS vs GCP vs Azure?", "Choose cloud provider",
            "S3 bucket setup", "Lambda functions guide",
            "Cloud architecture design", "Serverless deployment"
        ],
        "highly_relevant": [
            ("Recently deployed to AWS.", "task_history"),
            ("Working on cloud-native application.", "project_context"),
            ("Prefers AWS over other providers.", "preference")
        ],
        "somewhat_relevant": [
            ("Has experience in backend development.", "background"),
            ("Knows about microservices.", "background")
        ],
        "not_relevant": [
            ("Prefers vegetarian food.", "preference"),
            ("Enjoys morning jogs.", "preference")
        ]
    },
    {
        "category": "mobile_development",
        "prompts": [
            "Should I learn Flutter or React Native?", "Mobile app development guide",
            "iOS vs Android development", "Cross-platform framework",
            "Build mobile app from scratch", "Mobile UI best practices"
        ],
        "highly_relevant": [
            ("Interested in mobile development.", "preference"),
            ("Recently started learning Flutter.", "task_history"),
            ("Wants to build cross-platform app.", "project_context")
        ],
        "somewhat_relevant": [
            ("Knows JavaScript.", "background"),
            ("Has experience with UI design.", "background")
        ],
        "not_relevant": [
            ("Prefers vegetarian food.", "preference"),
            ("Last week searched for weekend trip ideas.", "temporal_event")
        ]
    },
    {
        "category": "code_documentation",
        "prompts": [
            "How to document my code?", "Write good README",
            "API documentation tools", "Code comments best practices",
            "Generate documentation automatically", "Swagger for APIs"
        ],
        "highly_relevant": [
            ("Recently wrote project documentation.", "task_history"),
            ("Working on open source project.", "project_context"),
            ("Values clear documentation.", "preference")
        ],
        "somewhat_relevant": [
            ("Has experience in backend development.", "background"),
            ("Working on team project.", "project_context")
        ],
        "not_relevant": [
            ("Prefers vegetarian food.", "preference"),
            ("Enjoys photography.", "preference")
        ]
    },
    {
        "category": "performance_monitoring",
        "prompts": [
            "Monitor app performance", "Set up logging and metrics",
            "APM tools comparison", "Track errors in production",
            "Performance monitoring best practices", "Prometheus and Grafana setup"
        ],
        "highly_relevant": [
            ("Recently implemented monitoring.", "task_history"),
            ("Working on production system.", "project_context"),
            ("Uses Grafana for dashboards.", "preference")
        ],
        "somewhat_relevant": [
            ("Has experience in backend development.", "background"),
            ("Working on AWAF dashboard backend.", "project_context")
        ],
        "not_relevant": [
            ("Prefers vegetarian food.", "preference"),
            ("Enjoys morning jogs.", "preference")
        ]
    },

    # ===== FOOD & NUTRITION (15 categories) =====
    {
        "category": "meal_suggestions",
        "prompts": [
            "Give me a healthy dinner idea", "Suggest a nutritious meal",
            "What should I cook for dinner tonight?", "Recommend a low-calorie dinner",
            "Quick and healthy recipe", "Meal prep ideas"
        ],
        "highly_relevant": [
            ("Prefers vegetarian food.", "preference"),
            ("Asked about meal under 500 calories.", "task_history"),
            ("Enjoys cooking with fresh ingredients.", "preference"),
            ("Has dietary restrictions: no dairy.", "preference")
        ],
        "somewhat_relevant": [
            ("Usually cooks dinner at 7 PM.", "device_context"),
            ("Shops for groceries on weekends.", "task_history")
        ],
        "not_relevant": [
            ("Prefers AMD CPUs for development.", "preference"),
            ("Working on AWAF dashboard backend.", "project_context"),
            ("Recently searched for laptop recommendations.", "task_history")
        ]
    },
    {
        "category": "diet_planning",
        "prompts": [
            "Create a diet plan for me", "Lose weight meal plan",
            "Nutrition guide for muscle gain", "Balanced diet suggestions",
            "Meal plan for the week", "Calorie deficit diet"
        ],
        "highly_relevant": [
            ("Wants to lose 5kg.", "preference"),
            ("Prefers vegetarian food.", "preference"),
            ("Tracks calories daily.", "preference"),
            ("Recently asked about nutrition.", "task_history")
        ],
        "somewhat_relevant": [
            ("Exercises 4 times a week.", "preference"),
            ("Usually free after 6 PM for meal prep.", "device_context")
        ],
        "not_relevant": [
            ("Prefers AMD CPUs.", "preference"),
            ("Working on backend project.", "project_context")
        ]
    },
    {
        "category": "recipe_requests",
        "prompts": [
            "How to make pasta?", "Simple breakfast recipes",
            "Quick lunch ideas", "Baking recipes for beginners",
            "Traditional Indian recipes", "Vegan dessert recipes"
        ],
        "highly_relevant": [
            ("Enjoys cooking with fresh ingredients.", "preference"),
            ("Prefers vegetarian food.", "preference"),
            ("Recently tried new recipes.", "task_history")
        ],
        "somewhat_relevant": [
            ("Usually cooks at home.", "preference"),
            ("Shops for groceries weekly.", "task_history")
        ],
        "not_relevant": [
            ("Knows Python programming.", "background"),
            ("Working on ML project.", "project_context")
        ]
    },
    {
        "category": "restaurant_recommendations",
        "prompts": [
            "Suggest a good restaurant nearby", "Best pizza place in town",
            "Where to eat tonight?", "Vegetarian restaurants",
            "Fancy dinner spot", "Cheap eats recommendations"
        ],
        "highly_relevant": [
            ("Prefers vegetarian food.", "preference"),
            ("Likes Italian cuisine.", "preference"),
            ("Lives in Mumbai.", "background"),
            ("Usually free after 6 PM.", "device_context")
        ],
        "somewhat_relevant": [
            ("Enjoys trying new foods.", "preference"),
            ("Goes out on weekends.", "preference")
        ],
        "not_relevant": [
            ("Working on backend project.", "project_context"),
            ("Prefers AMD CPUs.", "preference")
        ]
    },
    {
        "category": "nutritional_info",
        "prompts": [
            "Calories in banana", "Nutritional value of quinoa",
            "Is this food healthy?", "Protein content in eggs",
            "Compare nutritional values", "Vitamins in vegetables"
        ],
        "highly_relevant": [
            ("Tracks calories daily.", "preference"),
            ("Prefers vegetarian food.", "preference"),
            ("Recently asked about nutrition.", "task_history")
        ],
        "somewhat_relevant": [
            ("Wants to lose weight.", "preference"),
            ("Exercises regularly.", "preference")
        ],
        "not_relevant": [
            ("Working on ML project.", "project_context"),
            ("Knows Python programming.", "background")
        ]
    },
    {
        "category": "cooking_techniques",
        "prompts": [
            "How to sauté vegetables?", "Baking vs roasting",
            "Cooking techniques explained", "Perfect rice cooking",
            "Grilling tips", "Slow cooker recipes"
        ],
        "highly_relevant": [
            ("Enjoys cooking with fresh ingredients.", "preference"),
            ("Recently tried new cooking methods.", "task_history"),
            ("Wants to improve cooking skills.", "preference")
        ],
        "somewhat_relevant": [
            ("Usually cooks at home.", "preference"),
            ("Prefers vegetarian food.", "preference")
        ],
        "not_relevant": [
            ("Working on backend project.", "project_context"),
            ("Studies Computer Engineering.", "background")
        ]
    },
    {
        "category": "food_allergies",
        "prompts": [
            "Gluten-free alternatives", "Lactose-free recipes",
            "Nut allergy safe foods", "Allergy-friendly meal ideas",
            "Substitute for eggs in baking", "Dairy-free diet"
        ],
        "highly_relevant": [
            ("Has dietary restrictions: no dairy.", "preference"),
            ("Allergic to nuts.", "background"),
            ("Recently asked about allergies.", "task_history")
        ],
        "somewhat_relevant": [
            ("Prefers vegetarian food.", "preference"),
            ("Enjoys cooking.", "preference")
        ],
        "not_relevant": [
            ("Working on ML project.", "project_context"),
            ("Prefers AMD CPUs.", "preference")
        ]
    },
    {
        "category": "grocery_shopping",
        "prompts": [
            "Create grocery list", "Where to buy organic food?",
            "Budget grocery shopping tips", "Best supermarket nearby",
            "Online grocery delivery", "Meal prep shopping list"
        ],
        "highly_relevant": [
            ("Shops for groceries on weekends.", "task_history"),
            ("Prefers organic vegetables.", "preference"),
            ("Lives in Mumbai.", "background")
        ],
        "somewhat_relevant": [
            ("Prefers vegetarian food.", "preference"),
            ("Enjoys cooking at home.", "preference")
        ],
        "not_relevant": [
            ("Working on backend project.", "project_context"),
            ("Recently searched for laptop.", "task_history")
        ]
    },
    {
        "category": "food_preservation",
        "prompts": [
            "How to store vegetables?", "Food preservation methods",
            "Freeze leftover food", "Keep herbs fresh longer",
            "Pantry organization tips", "Meal prep storage"
        ],
        "highly_relevant": [
            ("Enjoys meal prepping.", "preference"),
            ("Recently asked about food storage.", "task_history"),
            ("Cooks in batches.", "preference")
        ],
        "somewhat_relevant": [
            ("Enjoys cooking at home.", "preference"),
            ("Shops for groceries weekly.", "task_history")
        ],
        "not_relevant": [
            ("Working on ML project.", "project_context"),
            ("Studies Computer Engineering.", "background")
        ]
    },
    {
        "category": "beverage_suggestions",
        "prompts": [
            "Healthy smoothie recipes", "Best coffee recommendations",
            "Homemade juice ideas", "Tea varieties explained",
            "Protein shake recipes", "Detox drinks"
        ],
        "highly_relevant": [
            ("Prefers coffee over tea.", "preference"),
            ("Drinks protein shakes post-workout.", "preference"),
            ("Recently asked about smoothies.", "task_history")
        ],
        "somewhat_relevant": [
            ("Exercises regularly.", "preference"),
            ("Enjoys healthy eating.", "preference")
        ],
        "not_relevant": [
            ("Working on backend project.", "project_context"),
            ("Prefers AMD CPUs.", "preference")
        ]
    },
    {
        "category": "international_cuisine",
        "prompts": [
            "Thai food recipes", "Italian cuisine guide",
            "Mexican dishes to try", "Japanese cooking basics",
            "Indian regional foods", "Chinese recipe suggestions"
        ],
        "highly_relevant": [
            ("Likes Italian cuisine.", "preference"),
            ("Visited Thailand last year.", "background"),
            ("Enjoys trying new cuisines.", "preference")
        ],
        "somewhat_relevant": [
            ("Enjoys cooking.", "preference"),
            ("Prefers vegetarian options.", "preference")
        ],
        "not_relevant": [
            ("Working on ML project.", "project_context"),
            ("Recently searched for laptop.", "task_history")
        ]
    },
    {
        "category": "meal_timing",
        "prompts": [
            "Best time to eat dinner?", "Intermittent fasting guide",
            "Meal timing for weight loss", "Pre-workout meal timing",
            "Late night snack ideas", "Breakfast importance"
        ],
        "highly_relevant": [
            ("Usually cooks dinner at 7 PM.", "device_context"),
            ("Practices intermittent fasting.", "preference"),
            ("Recently asked about meal timing.", "task_history")
        ],
        "somewhat_relevant": [
            ("Exercises in the morning.", "preference"),
            ("Wants to lose weight.", "preference")
        ],
        "not_relevant": [
            ("Working on backend project.", "project_context"),
            ("Studies Computer Engineering.", "background")
        ]
    },
    {
        "category": "food_budgeting",
        "prompts": [
            "Eat healthy on a budget", "Cheap meal ideas",
            "Save money on groceries", "Budget-friendly recipes",
            "Student meal planning", "Affordable nutrition"
        ],
        "highly_relevant": [
            ("Student with limited budget.", "background"),
            ("Shops for cheap groceries.", "preference"),
            ("Recently asked about budget meals.", "task_history")
        ],
        "somewhat_relevant": [
            ("Prefers vegetarian food.", "preference"),
            ("Enjoys cooking at home.", "preference")
        ],
        "not_relevant": [
            ("Working on ML project.", "project_context"),
            ("Prefers AMD CPUs.", "preference")
        ]
    },
    {
        "category": "special_diet",
        "prompts": [
            "Keto diet guide", "Paleo meal plan",
            "Mediterranean diet recipes", "Whole30 explained",
            "Plant-based diet tips", "Low-carb food ideas"
        ],
        "highly_relevant": [
            ("Following keto diet.", "preference"),
            ("Prefers low-carb meals.", "preference"),
            ("Recently asked about special diets.", "task_history")
        ],
        "somewhat_relevant": [
            ("Wants to lose weight.", "preference"),
            ("Tracks calories daily.", "preference")
        ],
        "not_relevant": [
            ("Working on backend project.", "project_context"),
            ("Studies Computer Engineering.", "background")
        ]
    },
    {
        "category": "food_photography",
        "prompts": [
            "How to photograph food?", "Food styling tips",
            "Instagram food photos", "Plating techniques",
            "Food photography lighting", "Make food look appetizing"
        ],
        "highly_relevant": [
            ("Enjoys food photography.", "preference"),
            ("Runs food Instagram account.", "background"),
            ("Recently asked about photo editing.", "task_history")
        ],
        "somewhat_relevant": [
            ("Enjoys cooking.", "preference"),
            ("Has good camera phone.", "device_context")
        ],
        "not_relevant": [
            ("Working on ML project.", "project_context"),
            ("Prefers AMD CPUs.", "preference")
        ]
    },

    # ===== FITNESS & HEALTH (20 categories) =====
    {
        "category": "workout_routines",
        "prompts": [
            "Recommend a workout routine", "Help me get fit",
            "Suggest exercises for beginners", "Create a fitness plan",
            "Gym workout schedule", "Home workout ideas"
        ],
        "highly_relevant": [
            ("Enjoys morning jogs in the park.", "preference"),
            ("Usually free after 6 PM for exercise.", "device_context"),
            ("Prefers low-impact exercises.", "preference"),
            ("Aims to exercise 4 times a week.", "preference")
        ],
        "somewhat_relevant": [
            ("Wants to lose weight.", "preference"),
            ("Recently joined a gym.", "task_history")
        ],
        "not_relevant": [
            ("Prefers AMD CPUs for development.", "preference"),
            ("Working on AWAF dashboard backend.", "project_context")
        ]
    },
    {
        "category": "weight_loss",
        "prompts": [
            "How to lose weight?", "Weight loss tips",
            "Lose 10 pounds in a month", "Fat burning exercises",
            "Healthy weight loss diet", "Weight loss plateau"
        ],
        "highly_relevant": [
            ("Wants to lose 5kg.", "preference"),
            ("Tracks calories daily.", "preference"),
            ("Recently started diet.", "task_history"),
            ("Aims to exercise 4 times a week.", "preference")
        ],
        "somewhat_relevant": [
            ("Prefers vegetarian food.", "preference"),
            ("Enjoys morning jogs.", "preference")
        ],
        "not_relevant": [
            ("Working on backend project.", "project_context"),
            ("Studies Computer Engineering.", "background")
        ]
    },
    {
        "category": "muscle_building",
        "prompts": [
            "Build muscle fast", "Muscle gain workout plan",
            "Best exercises for mass", "Protein for muscle growth",
            "Strength training guide", "Bodybuilding tips"
        ],
        "highly_relevant": [
            ("Wants to gain muscle.", "preference"),
            ("Drinks protein shakes post-workout.", "preference"),
            ("Recently joined gym for strength training.", "task_history")
        ],
        "somewhat_relevant": [
            ("Exercises 4 times a week.", "preference"),
            ("Tracks macros.", "preference")
        ],
        "not_relevant": [
            ("Prefers AMD CPUs.", "preference"),
            ("Working on ML project.", "project_context")
        ]
    },
    {
        "category": "cardio_exercises",
        "prompts": [
            "Best cardio for fat loss", "Running vs cycling",
            "HIIT workout guide", "Cardio at home",
            "Improve cardiovascular health", "Endurance training"
        ],
        "highly_relevant": [
            ("Enjoys morning jogs in the park.", "preference"),
            ("Recently started running.", "task_history"),
            ("Prefers cardio over weights.", "preference")
        ],
        "somewhat_relevant": [
            ("Wants to lose weight.", "preference"),
            ("Exercises regularly.", "preference")
        ],
        "not_relevant": [
            ("Working on backend project.", "project_context"),
            ("Prefers AMD CPUs.", "preference")
        ]
    },
    {
        "category": "yoga_flexibility",
        "prompts": [
            "Yoga for beginners", "Flexibility exercises",
            "Morning yoga routine", "Stretching guide",
            "Yoga poses for back pain", "Improve flexibility"
        ],
        "highly_relevant": [
            ("Practices yoga daily.", "preference"),
            ("Prefers low-impact exercises.", "preference"),
            ("Recently started yoga classes.", "task_history")
        ],
        "somewhat_relevant": [
            ("Exercises in the morning.", "preference"),
            ("Has yoga mat at home.", "device_context")
        ],
        "not_relevant": [
            ("Working on ML project.", "project_context"),
            ("Studies Computer Engineering.", "background")
        ]
    },
    {
        "category": "fitness_tracking",
        "prompts": [
            "Best fitness tracker app", "Track my workouts",
            "Fitness watch recommendations", "Monitor progress",
            "Calorie tracking app", "Fitness goals setting"
        ],
        "highly_relevant": [
            ("Uses Fitbit to track steps.", "device_context"),
            ("Tracks calories daily.", "preference"),
            ("Recently asked about fitness apps.", "task_history")
        ],
        "somewhat_relevant": [
            ("Aims to exercise 4 times a week.", "preference"),
            ("Wants to lose weight.", "preference")
        ],
        "not_relevant": [
            ("Working on backend project.", "project_context"),
            ("Prefers AMD CPUs.", "preference")
        ]
    },
    {
        "category": "sports_activities",
        "prompts": [
            "Learn to play tennis", "Basketball training tips",
            "Swimming techniques", "Soccer skills improvement",
            "Join sports club", "Outdoor sports ideas"
        ],
        "highly_relevant": [
            ("Plays basketball on weekends.", "preference"),
            ("Recently joined tennis club.", "task_history"),
            ("Enjoys team sports.", "preference")
        ],
        "somewhat_relevant": [
            ("Exercises regularly.", "preference"),
            ("Usually free after 6 PM.", "device_context")
        ],
        "not_relevant": [
            ("Working on ML project.", "project_context"),
            ("Prefers AMD CPUs.", "preference")
        ]
    },
    {
        "category": "recovery_rest",
        "prompts": [
            "Post-workout recovery", "Muscle soreness relief",
            "Rest day importance", "Foam rolling guide",
            "Sleep for recovery", "Prevent overtraining"
        ],
        "highly_relevant": [
            ("Experiences muscle soreness.", "preference"),
            ("Recently asked about recovery.", "task_history"),
            ("Uses foam roller.", "device_context")
        ],
        "somewhat_relevant": [
            ("Exercises 4 times a week.", "preference"),
            ("Sleeps 7-8 hours.", "preference")
        ],
        "not_relevant": [
            ("Working on backend project.", "project_context"),
            ("Studies Computer Engineering.", "background")
        ]
    },
    {
        "category": "injury_prevention",
        "prompts": [
            "Prevent workout injuries", "Safe exercise techniques",
            "Warm-up exercises", "Cool-down stretches",
            "Common gym injuries", "Proper form guide"
        ],
        "highly_relevant": [
            ("Recovering from knee injury.", "background"),
            ("Recently asked about injury prevention.", "task_history"),
            ("Prefers low-impact exercises.", "preference")
        ],
        "somewhat_relevant": [
            ("Exercises regularly.", "preference"),
            ("Recently joined gym.", "task_history")
        ],
        "not_relevant": [
            ("Working on ML project.", "project_context"),
            ("Prefers AMD CPUs.", "preference")
        ]
    },
    {
        "category": "mental_health",
        "prompts": [
            "Meditation for beginners", "Stress relief techniques",
            "Improve mental health", "Mindfulness practices",
            "Deal with anxiety", "Better sleep tips"
        ],
        "highly_relevant": [
            ("Practices meditation daily.", "preference"),
            ("Recently experiencing stress.", "task_history"),
            ("Uses Headspace app.", "device_context")
        ],
        "somewhat_relevant": [
            ("Practices yoga.", "preference"),
            ("Values work-life balance.", "preference")
        ],
        "not_relevant": [
            ("Working on backend project.", "project_context"),
            ("Prefers AMD CPUs.", "preference")
        ]
    },
    {
        "category": "hydration_nutrition",
        "prompts": [
            "How much water to drink?", "Hydration guide",
            "Pre-workout nutrition", "Post-workout meal",
            "Sports supplements", "Electrolyte drinks"
        ],
        "highly_relevant": [
            ("Drinks protein shakes post-workout.", "preference"),
            ("Recently asked about hydration.", "task_history"),
            ("Tracks water intake.", "preference")
        ],
        "somewhat_relevant": [
            ("Exercises 4 times a week.", "preference"),
            ("Wants to build muscle.", "preference")
        ],
        "not_relevant": [
            ("Working on ML project.", "project_context"),
            ("Studies Computer Engineering.", "background")
        ]
    },
    {
        "category": "fitness_motivation",
        "prompts": [
            "Stay motivated to exercise", "Fitness motivation tips",
            "Overcome workout laziness", "Find workout partner",
            "Set fitness goals", "Track fitness progress"
        ],
        "highly_relevant": [
            ("Recently lost motivation.", "task_history"),
            ("Aims to exercise 4 times a week.", "preference"),
            ("Joined accountability group.", "background")
        ],
        "somewhat_relevant": [
            ("Wants to lose weight.", "preference"),
            ("Recently joined gym.", "task_history")
        ],
        "not_relevant": [
            ("Working on backend project.", "project_context"),
            ("Prefers AMD CPUs.", "preference")
        ]
    },
    {
        "category": "outdoor_activities",
        "prompts": [
            "Hiking trails nearby", "Outdoor workout ideas",
            "Cycling routes", "Rock climbing beginners",
            "Camping fitness", "Adventure sports"
        ],
        "highly_relevant": [
            ("Enjoys hiking on weekends.", "preference"),
            ("Lives near mountains.", "background"),
            ("Recently bought hiking boots.", "task_history")
        ],
        "somewhat_relevant": [
            ("Enjoys outdoor activities.", "preference"),
            ("Usually free on weekends.", "device_context")
        ],
        "not_relevant": [
            ("Working on ML project.", "project_context"),
            ("Prefers AMD CPUs.", "preference")
        ]
    },
    {
        "category": "home_gym",
        "prompts": [
            "Set up home gym", "Home workout equipment",
            "Budget home gym", "Workout without equipment",
            "Space-saving gym setup", "Essential gym equipment"
        ],
        "highly_relevant": [
            ("Recently set up home gym.", "task_history"),
            ("Prefers working out at home.", "preference"),
            ("Has limited space.", "device_context")
        ],
        "somewhat_relevant": [
            ("Exercises regularly.", "preference"),
            ("Budget-conscious.", "preference")
        ],
        "not_relevant": [
            ("Working on backend project.", "project_context"),
            ("Studies Computer Engineering.", "background")
        ]
    },
    {
        "category": "fitness_classes",
        "prompts": [
            "Join fitness classes", "Zumba vs spinning",
            "CrossFit for beginners", "Pilates explained",
            "Group fitness benefits", "Online fitness classes"
        ],
        "highly_relevant": [
            ("Recently joined spin class.", "task_history"),
            ("Enjoys group workouts.", "preference"),
            ("Lives near fitness studio.", "background")
        ],
        "somewhat_relevant": [
            ("Exercises regularly.", "preference"),
            ("Usually free after 6 PM.", "device_context")
        ],
        "not_relevant": [
            ("Working on ML project.", "project_context"),
            ("Prefers AMD CPUs.", "preference")
        ]
    },
    {
        "category": "running_training",
        "prompts": [
            "Train for a marathon", "5K running plan",
            "Improve running speed", "Running form tips",
            "Running shoes guide", "Prevent running injuries"
        ],
        "highly_relevant": [
            ("Enjoys morning jogs in the park.", "preference"),
            ("Training for half marathon.", "preference"),
            ("Recently started running.", "task_history")
        ],
        "somewhat_relevant": [
            ("Prefers cardio exercises.", "preference"),
            ("Wants to improve endurance.", "preference")
        ],
        "not_relevant": [
            ("Working on backend project.", "project_context"),
            ("Prefers AMD CPUs.", "preference")
        ]
    },
    {
        "category": "strength_equipment",
        "prompts": [
            "Dumbbells vs barbells", "Kettlebell workout guide",
            "Resistance bands exercises", "Weight lifting basics",
            "Gym equipment explained", "Free weights vs machines"
        ],
        "highly_relevant": [
            ("Recently started weight training.", "task_history"),
            ("Wants to build muscle.", "preference"),
            ("Uses gym regularly.", "preference")
        ],
        "somewhat_relevant": [
            ("Exercises 4 times a week.", "preference"),
            ("Recently joined gym.", "task_history")
        ],
        "not_relevant": [
            ("Working on ML project.", "project_context"),
            ("Studies Computer Engineering.", "background")
        ]
    },
    {
        "category": "fitness_for_seniors",
        "prompts": [
            "Senior fitness guide", "Low-impact exercises for elderly",
            "Stay active after 60", "Senior yoga",
            "Balance exercises", "Safe workouts for seniors"
        ],
        "highly_relevant": [
            ("Over 60 years old.", "background"),
            ("Prefers low-impact exercises.", "preference"),
            ("Recently asked about senior fitness.", "task_history")
        ],
        "somewhat_relevant": [
            ("Has joint issues.", "background"),
            ("Practices yoga.", "preference")
        ],
        "not_relevant": [
            ("Working on ML project.", "project_context"),
            ("Student.", "background")
        ]
    },
    {
        "category": "fitness_challenges",
        "prompts": [
            "30-day fitness challenge", "Plank challenge",
            "Push-up challenge ideas", "Weight loss challenge",
            "Join fitness competition", "Transformation challenge"
        ],
        "highly_relevant": [
            ("Currently doing 30-day challenge.", "task_history"),
            ("Enjoys fitness challenges.", "preference"),
            ("Joined online fitness group.", "background")
        ],
        "somewhat_relevant": [
            ("Wants to lose weight.", "preference"),
            ("Exercises regularly.", "preference")
        ],
        "not_relevant": [
            ("Working on backend project.", "project_context"),
            ("Prefers AMD CPUs.", "preference")
        ]
    },
    {
        "category": "posture_ergonomics",
        "prompts": [
            "Improve posture", "Exercises for back pain",
            "Desk ergonomics", "Fix slouching",
            "Neck pain relief", "Standing desk benefits"
        ],
        "highly_relevant": [
            ("Experiences back pain from sitting.", "background"),
            ("Recently asked about posture.", "task_history"),
            ("Uses standing desk.", "device_context")
        ],
        "somewhat_relevant": [
            ("Works 8+ hours at computer.", "device_context"),
            ("Practices yoga.", "preference")
        ],
        "not_relevant": [
            ("Prefers AMD CPUs.", "preference"),
            ("Recently searched for laptop.", "task_history")
        ]
    },

    # ===== PRODUCTIVITY & LIFESTYLE (25 categories) =====
    {
        "category": "daily_planning",
        "prompts": [
            "Help me plan my day", "What should I focus on today?",
            "Create a schedule for today", "Suggest how to organize my day",
            "Daily routine optimization", "Time management tips"
        ],
        "highly_relevant": [
            ("Usually free after 6 PM.", "device_context"),
            ("Has reminder for project review meeting.", "device_context"),
            ("Asked earlier about improving productivity.", "task_history"),
            ("Reviewed notes for project submission.", "task_history")
        ],
        "somewhat_relevant": [
            ("Uses device mainly in IST timezone.", "device_context"),
            ("Stores files in organized project folders.", "device_context")
        ],
        "not_relevant": [
            ("Prefers minimal UI designs.", "preference"),
            ("Visited Thailand last year.", "background")
        ]
    },
    {
        "category": "study_routine",
        "prompts": [
            "Create a study routine for me", "How should I organize my learning?",
            "Help me plan my studies", "Suggest a productive study schedule",
            "Study tips for exams", "Learning strategy"
        ],
        "highly_relevant": [
            ("Studies Computer Engineering.", "background"),
            ("Participates in research groups at college.", "background"),
            ("Is learning AI model training techniques.", "background"),
            ("Reviewed notes for project submission.", "task_history")
        ],
        "somewhat_relevant": [
            ("Usually free after 6 PM.", "device_context"),
            ("Prefers studying in morning.", "preference")
        ],
        "not_relevant": [
            ("Prefers AMD CPUs for development.", "preference"),
            ("Visited Thailand last year.", "background")
        ]
    },
    {
        "category": "productivity_tools",
        "prompts": [
            "Best productivity apps", "Task management tools",
            "Note-taking app recommendations", "Project management software",
            "Calendar app comparison", "Productivity software"
        ],
        "highly_relevant": [
            ("Uses Notion for notes.", "device_context"),
            ("Asked earlier about improving productivity.", "task_history"),
            ("Recently tried productivity apps.", "task_history")
        ],
        "somewhat_relevant": [
            ("Syncs tasks across laptop and phone.", "device_context"),
            ("Stores files in organized folders.", "device_context")
        ],
        "not_relevant": [
            ("Prefers vegetarian food.", "preference"),
            ("Enjoys hiking.", "preference")
        ]
    },
    {
        "category": "time_blocking",
        "prompts": [
            "Time blocking method", "Schedule my work hours",
            "Deep work sessions", "Pomodoro technique",
            "Focus time management", "Block calendar for tasks"
        ],
        "highly_relevant": [
            ("Uses time blocking method.", "preference"),
            ("Asked earlier about improving productivity.", "task_history"),
            ("Has meetings scheduled regularly.", "device_context")
        ],
        "somewhat_relevant": [
            ("Usually free after 6 PM.", "device_context"),
            ("Works best in morning.", "preference")
        ],
        "not_relevant": [
            ("Prefers vegetarian food.", "preference"),
            ("Working on ML project.", "project_context")
        ]
    },
    {
        "category": "goal_setting",
        "prompts": [
            "Set personal goals", "SMART goals guide",
            "Track goal progress", "New year resolutions",
            "Long-term planning", "Achieve my goals"
        ],
        "highly_relevant": [
            ("Set goal to complete certification.", "preference"),
            ("Recently reviewed personal goals.", "task_history"),
            ("Uses goal tracking app.", "device_context")
        ],
        "somewhat_relevant": [
            ("Wants to improve productivity.", "preference"),
            ("Plans for career growth.", "background")
        ],
        "not_relevant": [
            ("Prefers AMD CPUs.", "preference"),
            ("Enjoys hiking.", "preference")
        ]
    },
    {
        "category": "habit_building",
        "prompts": [
            "Build good habits", "21-day habit challenge",
            "Break bad habits", "Habit tracking methods",
            "Morning routine habits", "Consistency tips"
        ],
        "highly_relevant": [
            ("Recently started habit tracking.", "task_history"),
            ("Uses habit tracker app.", "device_context"),
            ("Wants to build morning routine.", "preference")
        ],
        "somewhat_relevant": [
            ("Aims to exercise regularly.", "preference"),
            ("Values consistency.", "preference")
        ],
        "not_relevant": [
            ("Working on ML project.", "project_context"),
            ("Prefers AMD CPUs.", "preference")
        ]
    },
    {
        "category": "work_life_balance",
        "prompts": [
            "Improve work-life balance", "Avoid burnout",
            "Separate work and personal life", "Stress management",
            "Relaxation techniques", "Prevent overworking"
        ],
        "highly_relevant": [
            ("Recently feeling burned out.", "task_history"),
            ("Values work-life balance.", "preference"),
            ("Usually free after 6 PM.", "device_context")
        ],
        "somewhat_relevant": [
            ("Works long hours.", "device_context"),
            ("Practices meditation.", "preference")
        ],
        "not_relevant": [
            ("Prefers AMD CPUs.", "preference"),
            ("Visited Thailand.", "background")
        ]
    },
    {
        "category": "morning_routine",
        "prompts": [
            "Create morning routine", "Productive morning habits",
            "Wake up early tips", "Morning motivation",
            "Best morning activities", "Start day right"
        ],
        "highly_relevant": [
            ("Wakes up at 6 AM.", "preference"),
            ("Enjoys morning jogs.", "preference"),
            ("Recently asked about morning routine.", "task_history")
        ],
        "somewhat_relevant": [
            ("Practices yoga in morning.", "preference"),
            ("Prefers studying in morning.", "preference")
        ],
        "not_relevant": [
            ("Working on ML project.", "project_context"),
            ("Prefers AMD CPUs.", "preference")
        ]
    },
    {
        "category": "evening_routine",
        "prompts": [
            "Evening routine suggestions", "Wind down before bed",
            "Night-time productivity", "Prepare for tomorrow",
            "Relax after work", "Evening habits"
        ],
        "highly_relevant": [
            ("Usually free after 6 PM.", "device_context"),
            ("Struggles with sleep.", "preference"),
            ("Recently asked about evening routine.", "task_history")
        ],
        "somewhat_relevant": [
            ("Practices meditation before bed.", "preference"),
            ("Reads before sleeping.", "preference")
        ],
        "not_relevant": [
            ("Working on ML project.", "project_context"),
            ("Prefers AMD CPUs.", "preference")
        ]
    },
    {
        "category": "focus_concentration",
        "prompts": [
            "Improve focus", "Concentration techniques",
            "Avoid distractions", "Deep work guide",
            "Stay focused while studying", "Minimize interruptions"
        ],
        "highly_relevant": [
            ("Easily distracted.", "preference"),
            ("Recently asked about focus techniques.", "task_history"),
            ("Uses focus apps.", "device_context")
        ],
        "somewhat_relevant": [
            ("Studies Computer Engineering.", "background"),
            ("Works on complex projects.", "project_context")
        ],
        "not_relevant": [
            ("Prefers vegetarian food.", "preference"),
            ("Enjoys hiking.", "preference")
        ]
    },
    {
        "category": "procrastination",
        "prompts": [
            "Stop procrastinating", "Overcome procrastination",
            "Get started on tasks", "Beat laziness",
            "Motivation to work", "Procrastination psychology"
        ],
        "highly_relevant": [
            ("Struggles with procrastination.", "preference"),
            ("Recently asked about motivation.", "task_history"),
            ("Has pending tasks.", "task_history")
        ],
        "somewhat_relevant": [
            ("Wants to improve productivity.", "preference"),
            ("Uses task management apps.", "device_context")
        ],
        "not_relevant": [
            ("Working on ML project.", "project_context"),
            ("Prefers AMD CPUs.", "preference")
        ]
    },
    {
        "category": "email_management",
        "prompts": [
            "Manage email efficiently", "Inbox zero method",
            "Email organization tips", "Reduce email time",
            "Email productivity", "Filter spam emails"
        ],
        "highly_relevant": [
            ("Overwhelmed by emails.", "task_history"),
            ("Recently asked about email management.", "task_history"),
            ("Uses Gmail filters.", "device_context")
        ],
        "somewhat_relevant": [
            ("Wants to improve productivity.", "preference"),
            ("Checks email frequently.", "preference")
        ],
        "not_relevant": [
            ("Prefers vegetarian food.", "preference"),
            ("Enjoys hiking.", "preference")
        ]
    },
    {
        "category": "meeting_productivity",
        "prompts": [
            "Run effective meetings", "Meeting productivity tips",
            "Avoid unnecessary meetings", "Meeting agenda template",
            "Virtual meeting best practices", "Meeting notes organization"
        ],
        "highly_relevant": [
            ("Has reminder for project review meeting.", "device_context"),
            ("Attends many meetings.", "task_history"),
            ("Recently asked about meeting efficiency.", "task_history")
        ],
        "somewhat_relevant": [
            ("Works on team projects.", "project_context"),
            ("Uses calendar actively.", "device_context")
        ],
        "not_relevant": [
            ("Prefers vegetarian food.", "preference"),
            ("Enjoys hiking.", "preference")
        ]
    },
    {
        "category": "digital_minimalism",
        "prompts": [
            "Digital detox tips", "Reduce screen time",
            "Minimize digital distractions", "Social media break",
            "Phone addiction help", "Digital wellbeing"
        ],
        "highly_relevant": [
            ("Spends too much time on phone.", "preference"),
            ("Recently asked about screen time.", "task_history"),
            ("Uses screen time tracking.", "device_context")
        ],
        "somewhat_relevant": [
            ("Values work-life balance.", "preference"),
            ("Wants to reduce distractions.", "preference")
        ],
        "not_relevant": [
            ("Working on ML project.", "project_context"),
            ("Prefers AMD CPUs.", "preference")
        ]
    },
    {
        "category": "decision_making",
        "prompts": [
            "Make better decisions", "Decision-making frameworks",
            "Analyze choices effectively", "Pros and cons method",
            "Overcome analysis paralysis", "Quick decision strategies"
        ],
        "highly_relevant": [
            ("Struggles with decision-making.", "preference"),
            ("Recently asked about decision frameworks.", "task_history"),
            ("Has major decision pending.", "task_history")
        ],
        "somewhat_relevant": [
            ("Values logical thinking.", "preference"),
            ("Overthinks often.", "preference")
        ],
        "not_relevant": [
            ("Prefers vegetarian food.", "preference"),
            ("Working on ML project.", "project_context")
        ]
    },
    {
        "category": "creativity_boost",
        "prompts": [
            "Boost creativity", "Creative thinking techniques",
            "Overcome creative block", "Innovation methods",
            "Brainstorming strategies", "Think outside the box"
        ],
        "highly_relevant": [
            ("Recently experienced creative block.", "task_history"),
            ("Works on creative projects.", "project_context"),
            ("Values creative problem-solving.", "preference")
        ],
        "somewhat_relevant": [
            ("Works on innovative solutions.", "project_context"),
            ("Enjoys brainstorming.", "preference")
        ],
        "not_relevant": [
            ("Prefers vegetarian food.", "preference"),
            ("Usually free after 6 PM.", "device_context")
        ]
    },
    {
        "category": "learning_methods",
        "prompts": [
            "Effective learning techniques", "How to learn faster",
            "Study methods comparison", "Active recall technique",
            "Spaced repetition system", "Learning retention tips"
        ],
        "highly_relevant": [
            ("Is learning AI model training techniques.", "background"),
            ("Recently asked about learning methods.", "task_history"),
            ("Uses Anki for spaced repetition.", "device_context")
        ],
        "somewhat_relevant": [
            ("Studies Computer Engineering.", "background"),
            ("Takes online courses.", "background")
        ],
        "not_relevant": [
            ("Prefers vegetarian food.", "preference"),
            ("Enjoys hiking.", "preference")
        ]
    },
    {
        "category": "reading_habits",
        "prompts": [
            "Build reading habit", "Read more books",
            "Speed reading techniques", "Book recommendations",
            "Reading goals", "Find time to read"
        ],
        "highly_relevant": [
            ("Wants to read more.", "preference"),
            ("Recently joined book club.", "background"),
            ("Set goal to read 24 books this year.", "preference")
        ],
        "somewhat_relevant": [
            ("Enjoys learning.", "preference"),
            ("Reads before bed.", "preference")
        ],
        "not_relevant": [
            ("Working on ML project.", "project_context"),
            ("Prefers AMD CPUs.", "preference")
        ]
    },
    {
        "category": "sleep_optimization",
        "prompts": [
            "Improve sleep quality", "Sleep better tips",
            "Sleep hygiene guide", "Insomnia solutions",
            "Sleep schedule optimization", "Wake up refreshed"
        ],
        "highly_relevant": [
            ("Struggles with sleep.", "preference"),
            ("Recently asked about sleep quality.", "task_history"),
            ("Uses sleep tracking app.", "device_context")
        ],
        "somewhat_relevant": [
            ("Practices meditation before bed.", "preference"),
            ("Wants to wake up early.", "preference")
        ],
        "not_relevant": [
            ("Working on ML project.", "project_context"),
            ("Prefers AMD CPUs.", "preference")
        ]
    },
    {
        "category": "financial_planning",
        "prompts": [
            "Budget planning tips", "Save money effectively",
            "Personal finance guide", "Investment for beginners",
            "Track expenses", "Financial goals setting"
        ],
        "highly_relevant": [
            ("Recently asked about budgeting.", "task_history"),
            ("Wants to save for laptop.", "preference"),
            ("Uses expense tracking app.", "device_context")
        ],
        "somewhat_relevant": [
            ("Student with limited budget.", "background"),
            ("Plans to invest.", "preference")
        ],
        "not_relevant": [
            ("Working on ML project.", "project_context"),
            ("Enjoys hiking.", "preference")
        ]
    },
    {
        "category": "career_development",
        "prompts": [
            "Career advice", "Switch careers guidance",
            "Skill development plan", "Job search strategies",
            "Career growth tips", "Professional development"
        ],
        "highly_relevant": [
            ("Planning career switch to ML.", "preference"),
            ("Recently asked about career options.", "task_history"),
            ("Wants to upskill.", "preference")
        ],
        "somewhat_relevant": [
            ("Studies Computer Engineering.", "background"),
            ("Has experience in backend development.", "background")
        ],
        "not_relevant": [
            ("Prefers vegetarian food.", "preference"),
            ("Enjoys hiking.", "preference")
        ]
    },
    {
        "category": "networking_skills",
        "prompts": [
            "Professional networking tips", "LinkedIn optimization",
            "Build professional connections", "Networking events",
            "Cold email techniques", "Grow professional network"
        ],
        "highly_relevant": [
            ("Recently updated LinkedIn.", "task_history"),
            ("Wants to expand network.", "preference"),
            ("Attending tech conference next month.", "task_history")
        ],
        "somewhat_relevant": [
            ("Works in tech industry.", "background"),
            ("Values professional relationships.", "preference")
        ],
        "not_relevant": [
            ("Prefers vegetarian food.", "preference"),
            ("Working on ML project.", "project_context")
        ]
    },
    {
        "category": "remote_work",
        "prompts": [
            "Remote work productivity", "Work from home setup",
            "Virtual collaboration tips", "Home office organization",
            "Remote work best practices", "Stay productive at home"
        ],
        "highly_relevant": [
            ("Works remotely full-time.", "background"),
            ("Recently set up home office.", "task_history"),
            ("Uses standing desk.", "device_context")
        ],
        "somewhat_relevant": [
            ("Values work-life balance.", "preference"),
            ("Uses productivity tools.", "device_context")
        ],
        "not_relevant": [
            ("Prefers vegetarian food.", "preference"),
            ("Enjoys hiking.", "preference")
        ]
    },
    {
        "category": "minimalism_declutter",
        "prompts": [
            "Declutter living space", "Minimalism guide",
            "Organize home efficiently", "Marie Kondo method",
            "Reduce possessions", "Simple living tips"
        ],
        "highly_relevant": [
            ("Recently started decluttering.", "task_history"),
            ("Values minimalism.", "preference"),
            ("Wants to organize better.", "preference")
        ],
        "somewhat_relevant": [
            ("Lives in small apartment.", "background"),
            ("Prefers simple lifestyle.", "preference")
        ],
        "not_relevant": [
            ("Working on ML project.", "project_context"),
            ("Prefers AMD CPUs.", "preference")
        ]
    },
    {
        "category": "journaling_reflection",
        "prompts": [
            "Start journaling habit", "Daily reflection practice",
            "Gratitude journaling", "Bullet journaling guide",
            "Journaling prompts", "Self-reflection methods"
        ],
        "highly_relevant": [
            ("Recently started journaling.", "task_history"),
            ("Uses journaling app.", "device_context"),
            ("Values self-reflection.", "preference")
        ],
        "somewhat_relevant": [
            ("Wants to build morning routine.", "preference"),
            ("Practices mindfulness.", "preference")
        ],
        "not_relevant": [
            ("Working on ML project.", "project_context"),
            ("Prefers AMD CPUs.", "preference")
        ]
    },

    # ===== TRAVEL & EXPLORATION (15 categories) =====
    {
        "category": "travel_planning",
        "prompts": [
            "Recommend a travel destination", "Where should I go for vacation?",
            "Suggest a weekend trip", "Plan a travel itinerary for me",
            "Budget travel destinations", "Solo travel ideas"
        ],
        "highly_relevant": [
            ("Last week searched for weekend trip ideas.", "temporal_event"),
            ("Visited Thailand last year.", "background"),
            ("Enjoys exploring new cultures.", "preference"),
            ("Prefers beach destinations over mountains.", "preference")
        ],
        "somewhat_relevant": [
            ("Usually free on weekends.", "device_context"),
            ("Budget is around $1000 for trips.", "preference")
        ],
        "not_relevant": [
            ("Prefers AMD CPUs for development.", "preference"),
            ("Working on AWAF dashboard backend.", "project_context")
        ]
    },
    {
        "category": "travel_budgeting",
        "prompts": [
            "Budget travel tips", "Cheap vacation ideas",
            "Save money while traveling", "Affordable destinations",
            "Travel on a budget", "Cost-effective travel"
        ],
        "highly_relevant": [
            ("Budget is around $1000 for trips.", "preference"),
            ("Recently asked about budget travel.", "task_history"),
            ("Student with limited budget.", "background")
        ],
        "somewhat_relevant": [
            ("Enjoys traveling.", "preference"),
            ("Plans trips frequently.", "preference")
        ],
        "not_relevant": [
            ("Working on ML project.", "project_context"),
            ("Prefers AMD CPUs.", "preference")
        ]
    },
    {
        "category": "travel_packing",
        "prompts": [
            "Packing list for trip", "How to pack efficiently",
            "Travel packing tips", "Carry-on only packing",
            "Essential travel items", "Minimalist packing"
        ],
        "highly_relevant": [
            ("Traveling next week.", "task_history"),
            ("Recently asked about packing.", "task_history"),
            ("Prefers carry-on only.", "preference")
        ],
        "somewhat_relevant": [
            ("Enjoys traveling.", "preference"),
            ("Values minimalism.", "preference")
        ],
        "not_relevant": [
            ("Working on ML project.", "project_context"),
            ("Prefers AMD CPUs.", "preference")
        ]
    },
    {
        "category": "flight_booking",
        "prompts": [
            "Find cheap flights", "Best time to book flights",
            "Flight booking tips", "Compare flight prices",
            "Travel credit cards", "Airline rewards programs"
        ],
        "highly_relevant": [
            ("Planning international trip.", "task_history"),
            ("Recently searched for flights.", "task_history"),
            ("Uses flight comparison sites.", "preference")
        ],
        "somewhat_relevant": [
            ("Travels frequently.", "preference"),
            ("Budget-conscious.", "preference")
        ],
        "not_relevant": [
            ("Working on ML project.", "project_context"),
            ("Prefers vegetarian food.", "preference")
        ]
    },
    {
        "category": "accommodation_booking",
        "prompts": [
            "Find hotels", "Airbnb vs hotel",
            "Budget accommodation", "Hostel recommendations",
            "Book vacation rental", "Best hotel deals"
        ],
        "highly_relevant": [
            ("Planning trip next month.", "task_history"),
            ("Prefers Airbnb over hotels.", "preference"),
            ("Recently booked accommodation.", "task_history")
        ],
        "somewhat_relevant": [
            ("Budget-conscious traveler.", "preference"),
            ("Enjoys solo travel.", "preference")
        ],
        "not_relevant": [
            ("Working on ML project.", "project_context"),
            ("Prefers AMD CPUs.", "preference")
        ]
    },
    {
        "category": "solo_travel",
        "prompts": [
            "Solo travel tips", "Safe destinations for solo travelers",
            "First solo trip advice", "Meet people while traveling",
            "Solo travel benefits", "Overcome travel anxiety"
        ],
        "highly_relevant": [
            ("Planning first solo trip.", "task_history"),
            ("Enjoys solo travel.", "preference"),
            ("Recently asked about safety.", "task_history")
        ],
        "somewhat_relevant": [
            ("Traveled alone before.", "background"),
            ("Enjoys exploring.", "preference")
        ],
        "not_relevant": [
            ("Working on ML project.", "project_context"),
            ("Prefers AMD CPUs.", "preference")
        ]
    },
    {
        "category": "travel_photography",
        "prompts": [
            "Travel photography tips", "Best camera for travel",
            "Photography while traveling", "Instagram travel photos",
            "Capture moments better", "Photography equipment travel"
        ],
        "highly_relevant": [
            ("Enjoys photography.", "preference"),
            ("Recently bought camera.", "task_history"),
            ("Plans to document trip.", "task_history")
        ],
        "somewhat_relevant": [
            ("Enjoys traveling.", "preference"),
            ("Uses Instagram actively.", "background")
        ],
        "not_relevant": [
            ("Working on ML project.", "project_context"),
            ("Prefers vegetarian food.", "preference")
        ]
    },
    {
        "category": "cultural_experiences",
        "prompts": [
            "Experience local culture", "Cultural immersion tips",
            "Learn about traditions", "Local customs guide",
            "Authentic travel experiences", "Cultural sensitivity"
        ],
        "highly_relevant": [
            ("Enjoys exploring new cultures.", "preference"),
            ("Visited Thailand last year.", "background"),
            ("Values authentic experiences.", "preference")
        ],
        "somewhat_relevant": [
            ("Enjoys traveling.", "preference"),
            ("Learning new languages.", "preference")
        ],
        "not_relevant": [
            ("Working on ML project.", "project_context"),
            ("Prefers AMD CPUs.", "preference")
        ]
    },
    {
        "category": "adventure_travel",
        "prompts": [
            "Adventure travel ideas", "Extreme sports destinations",
            "Hiking and trekking trips", "Adventure activities",
            "Thrilling experiences", "Outdoor adventures"
        ],
        "highly_relevant": [
            ("Enjoys adventure sports.", "preference"),
            ("Recently went trekking.", "task_history"),
            ("Plans to try skydiving.", "preference")
        ],
        "somewhat_relevant": [
            ("Enjoys hiking.", "preference"),
            ("Physically active.", "preference")
        ],
        "not_relevant": [
            ("Working on ML project.", "project_context"),
            ("Prefers vegetarian food.", "preference")
        ]
    },
    {
        "category": "beach_destinations",
        "prompts": [
            "Best beach destinations", "Tropical vacation ideas",
            "Beach resorts recommendations", "Island hopping guide",
            "Coastal travel", "Seaside getaways"
        ],
        "highly_relevant": [
            ("Prefers beach destinations over mountains.", "preference"),
            ("Recently searched for beaches.", "task_history"),
            ("Loves swimming.", "preference")
        ],
        "somewhat_relevant": [
            ("Enjoys warm weather.", "preference"),
            ("Relaxation travel.", "preference")
        ],
        "not_relevant": [
            ("Working on ML project.", "project_context"),
            ("Prefers AMD CPUs.", "preference")
        ]
    },
    {
        "category": "travel_safety",
        "prompts": [
            "Travel safety tips", "Stay safe abroad",
            "Avoid travel scams", "Safe destinations",
            "Travel insurance guide", "Emergency preparedness"
        ],
        "highly_relevant": [
            ("Planning first international trip.", "task_history"),
            ("Recently asked about safety.", "task_history"),
            ("Values travel insurance.", "preference")
        ],
        "somewhat_relevant": [
            ("Solo traveler.", "preference"),
            ("Cautious person.", "preference")
        ],
        "not_relevant": [
            ("Working on ML project.", "project_context"),
            ("Prefers AMD CPUs.", "preference")
        ]
    },
    {
        "category": "visa_requirements",
        "prompts": [
            "Visa requirements", "How to apply for visa",
            "Visa-free countries", "Travel documents needed",
            "Passport renewal", "Immigration process"
        ],
        "highly_relevant": [
            ("Planning international trip.", "task_history"),
            ("Recently checked visa requirements.", "task_history"),
            ("Lives in India.", "background")
        ],
        "somewhat_relevant": [
            ("Travels internationally.", "preference"),
            ("Has valid passport.", "background")
        ],
        "not_relevant": [
            ("Working on ML project.", "project_context"),
            ("Prefers vegetarian food.", "preference")
        ]
    },
    {
        "category": "local_transportation",
        "prompts": [
            "Getting around in new city", "Public transportation tips",
            "Rent a car abroad", "Navigate foreign cities",
            "Transportation options", "Local transit guide"
        ],
        "highly_relevant": [
            ("Traveling to new city next week.", "task_history"),
            ("Recently asked about transportation.", "task_history"),
            ("Prefers public transport.", "preference")
        ],
        "somewhat_relevant": [
            ("Budget-conscious traveler.", "preference"),
            ("Enjoys exploring cities.", "preference")
        ],
        "not_relevant": [
            ("Working on ML project.", "project_context"),
            ("Prefers AMD CPUs.", "preference")
        ]
    },
    {
        "category": "travel_language",
        "prompts": [
            "Learn travel phrases", "Language basics for travel",
            "Translation apps", "Communicate abroad",
            "Essential foreign phrases", "Language barrier tips"
        ],
        "highly_relevant": [
            ("Traveling to Japan next month.", "task_history"),
            ("Learning basic Japanese.", "task_history"),
            ("Uses translation apps.", "device_context")
        ],
        "somewhat_relevant": [
            ("Enjoys learning languages.", "preference"),
            ("Values cultural immersion.", "preference")
        ],
        "not_relevant": [
            ("Working on ML project.", "project_context"),
            ("Prefers AMD CPUs.", "preference")
        ]
    },
    {
        "category": "sustainable_travel",
        "prompts": [
            "Eco-friendly travel", "Sustainable tourism",
            "Reduce carbon footprint travel", "Responsible travel tips",
            "Green travel practices", "Ethical tourism"
        ],
        "highly_relevant": [
            ("Values sustainable travel.", "preference"),
            ("Recently asked about eco-tourism.", "task_history"),
            ("Avoids flights when possible.", "preference")
        ],
        "somewhat_relevant": [
            ("Environmentally conscious.", "preference"),
            ("Supports local businesses.", "preference")
        ],
        "not_relevant": [
            ("Working on ML project.", "project_context"),
            ("Prefers AMD CPUs.", "preference")
        ]
    },

    # ===== ENTERTAINMENT & HOBBIES (20 categories) =====
    {
        "category": "music_recommendations",
        "prompts": [
            "Music recommendations", "New songs to listen to",
            "Best playlists", "Discover new artists",
            "Music for studying", "Workout music"
        ],
        "highly_relevant": [
            ("Listens to indie rock.", "preference"),
            ("Uses Spotify daily.", "device_context"),
            ("Recently asked for music recs.", "task_history")
        ],
        "somewhat_relevant": [
            ("Enjoys music while coding.", "preference"),
            ("Creates playlists.", "preference")
        ],
        "not_relevant": [
            ("Working on ML project.", "project_context"),
            ("Prefers vegetarian food.", "preference")
        ]
    },
    {
        "category": "movie_recommendations",
        "prompts": [
            "Movie recommendations", "What to watch tonight",
            "Best movies on Netflix", "Film suggestions",
            "Classic movies to watch", "Movie genres explained"
        ],
        "highly_relevant": [
            ("Likes sci-fi movies.", "preference"),
            ("Recently asked for movie recs.", "task_history"),
            ("Has Netflix subscription.", "device_context")
        ],
        "somewhat_relevant": [
            ("Enjoys watching movies on weekends.", "preference"),
            ("Prefers thriller genres.", "preference")
        ],
        "not_relevant": [
            ("Working on ML project.", "project_context"),
            ("Prefers vegetarian food.", "preference")
        ]
    },
    {
        "category": "gaming_recommendations",
        "prompts": [
            "Game recommendations", "Best PC games",
            "Multiplayer games to try", "Gaming setup advice",
            "New releases worth playing", "Indie games"
        ],
        "highly_relevant": [
            ("Enjoys gaming.", "preference"),
            ("Recently bought gaming laptop.", "task_history"),
            ("Plays on Steam.", "device_context")
        ],
        "somewhat_relevant": [
            ("Enjoys multiplayer games.", "preference"),
            ("Usually games on weekends.", "device_context")
        ],
        "not_relevant": [
            ("Prefers vegetarian food.", "preference"),
            ("Exercises regularly.", "preference")
        ]
    },
    {
        "category": "book_recommendations",
        "prompts": [
            "Book recommendations", "What to read next",
            "Best fiction books", "Non-fiction suggestions",
            "Book club ideas", "Reading list"
        ],
        "highly_relevant": [
            ("Enjoys sci-fi novels.", "preference"),
            ("Recently finished a book.", "task_history"),
            ("Joined book club.", "background")
        ],
        "somewhat_relevant": [
            ("Reads before bed.", "preference"),
            ("Set goal to read 24 books.", "preference")
        ],
        "not_relevant": [
            ("Working on ML project.", "project_context"),
            ("Prefers AMD CPUs.", "preference")
        ]
    },
    {
        "category": "podcast_recommendations",
        "prompts": [
            "Podcast recommendations", "Best podcasts to listen",
            "Tech podcasts", "True crime podcasts",
            "Educational podcasts", "Comedy podcasts"
        ],
        "highly_relevant": [
            ("Listens to tech podcasts.", "preference"),
            ("Recently subscribed to podcasts.", "task_history"),
            ("Listens while commuting.", "preference")
        ],
        "somewhat_relevant": [
            ("Enjoys learning new things.", "preference"),
            ("Uses podcast apps.", "device_context")
        ],
        "not_relevant": [
            ("Working on ML project.", "project_context"),
            ("Prefers vegetarian food.", "preference")
        ]
    },
    {
        "category": "photography_hobby",
        "prompts": [
            "Photography tips for beginners", "Camera recommendations",
            "Improve photography skills", "Photo editing apps",
            "Photography techniques", "Portrait photography"
        ],
        "highly_relevant": [
            ("Enjoys photography.", "preference"),
            ("Recently bought DSLR camera.", "task_history"),
            ("Uses Lightroom for editing.", "device_context")
        ],
        "somewhat_relevant": [
            ("Interested in visual arts.", "preference"),
            ("Shares photos on Instagram.", "background")
        ],
        "not_relevant": [
            ("Working on ML project.", "project_context"),
            ("Prefers vegetarian food.", "preference")
        ]
    },
    {
        "category": "cooking_hobby",
        "prompts": [
            "Learn cooking skills", "Cooking classes",
            "Advanced cooking techniques", "Culinary skills",
            "Master chef tips", "Cooking as hobby"
        ],
        "highly_relevant": [
            ("Enjoys cooking.", "preference"),
            ("Recently took cooking class.", "task_history"),
            ("Wants to improve cooking skills.", "preference")
        ],
        "somewhat_relevant": [
            ("Cooks at home daily.", "preference"),
            ("Tries new recipes.", "preference")
        ],
        "not_relevant": [
            ("Working on ML project.", "project_context"),
            ("Prefers AMD CPUs.", "preference")
        ]
    },
    {
        "category": "art_craft",
        "prompts": [
            "Art and craft ideas", "Learn painting",
            "DIY projects", "Creative hobbies",
            "Drawing tutorials", "Craft supplies"
        ],
        "highly_relevant": [
            ("Enjoys painting.", "preference"),
            ("Recently started art classes.", "task_history"),
            ("Has art supplies at home.", "device_context")
        ],
        "somewhat_relevant": [
            ("Interested in creative activities.", "preference"),
            ("Values artistic expression.", "preference")
        ],
        "not_relevant": [
            ("Working on ML project.", "project_context"),
            ("Prefers vegetarian food.", "preference")
        ]
    },
    {
        "category": "gardening",
        "prompts": [
            "Gardening for beginners", "Indoor plants care",
            "Vegetable gardening", "Plant recommendations",
            "Garden maintenance", "Grow herbs at home"
        ],
        "highly_relevant": [
            ("Enjoys gardening.", "preference"),
            ("Recently started indoor garden.", "task_history"),
            ("Has balcony space for plants.", "device_context")
        ],
        "somewhat_relevant": [
            ("Interested in sustainability.", "preference"),
            ("Lives in apartment.", "background")
        ],
        "not_relevant": [
            ("Working on ML project.", "project_context"),
            ("Prefers AMD CPUs.", "preference")
        ]
    },
    {
        "category": "musical_instruments",
        "prompts": [
            "Learn guitar", "Piano lessons for beginners",
            "Music theory basics", "Practice techniques",
            "Choose musical instrument", "Online music lessons"
        ],
        "highly_relevant": [
            ("Learning guitar.", "preference"),
            ("Recently bought acoustic guitar.", "task_history"),
            ("Practices daily.", "preference")
        ],
        "somewhat_relevant": [
            ("Enjoys music.", "preference"),
            ("Has musical background.", "background")
        ],
        "not_relevant": [
            ("Working on ML project.", "project_context"),
            ("Prefers vegetarian food.", "preference")
        ]
    },
    {
        "category": "writing_creative",
        "prompts": [
            "Creative writing tips", "Start writing a novel",
            "Blogging guide", "Improve writing skills",
            "Writing prompts", "Storytelling techniques"
        ],
        "highly_relevant": [
            ("Enjoys creative writing.", "preference"),
            ("Recently started blog.", "background"),
            ("Writes daily.", "preference")
        ],
        "somewhat_relevant": [
            ("Wants to publish book.", "preference"),
            ("Enjoys reading.", "preference")
        ],
        "not_relevant": [
            ("Working on ML project.", "project_context"),
            ("Prefers AMD CPUs.", "preference")
        ]
    },
    {
        "category": "sports_watching",
        "prompts": [
            "Sports to watch", "Follow cricket matches",
            "Football leagues", "Sports streaming",
            "Best sports moments", "Upcoming matches"
        ],
        "highly_relevant": [
            ("Follows cricket actively.", "preference"),
            ("Watches IPL matches.", "preference"),
            ("Recently subscribed to sports channel.", "task_history")
        ],
        "somewhat_relevant": [
            ("Enjoys watching sports on weekends.", "preference"),
            ("Supports specific teams.", "preference")
        ],
        "not_relevant": [
            ("Working on ML project.", "project_context"),
            ("Prefers vegetarian food.", "preference")
        ]
    },
    {
        "category": "board_games",
        "prompts": [
            "Board game recommendations", "Strategy games",
            "Party games ideas", "Chess improvement",
            "Card games to play", "Tabletop gaming"
        ],
        "highly_relevant": [
            ("Enjoys board games.", "preference"),
            ("Recently bought new games.", "task_history"),
            ("Hosts game nights.", "preference")
        ],
        "somewhat_relevant": [
            ("Enjoys social activities.", "preference"),
            ("Likes strategic thinking.", "preference")
        ],
        "not_relevant": [
            ("Working on ML project.", "project_context"),
            ("Prefers vegetarian food.", "preference")
        ]
    },
    {
        "category": "collecting_hobbies",
        "prompts": [
            "Start collecting hobby", "Coin collecting guide",
            "Stamp collecting", "Collectibles value",
            "Build collection", "Rare items hunting"
        ],
        "highly_relevant": [
            ("Collects vintage cameras.", "preference"),
            ("Recently bought collector item.", "task_history"),
            ("Enjoys hunting for antiques.", "preference")
        ],
        "somewhat_relevant": [
            ("Visits flea markets.", "preference"),
            ("Interested in history.", "preference")
        ],
        "not_relevant": [
            ("Working on ML project.", "project_context"),
            ("Prefers vegetarian food.", "preference")
        ]
    },
    {
        "category": "meditation_mindfulness",
        "prompts": [
            "Meditation for beginners", "Mindfulness practices",
            "Guided meditation", "Breathing exercises",
            "Meditation apps", "Calm mind techniques"
        ],
        "highly_relevant": [
            ("Practices meditation daily.", "preference"),
            ("Uses Headspace app.", "device_context"),
            ("Recently started mindfulness practice.", "task_history")
        ],
        "somewhat_relevant": [
            ("Values mental health.", "preference"),
            ("Practices yoga.", "preference")
        ],
        "not_relevant": [
            ("Working on ML project.", "project_context"),
            ("Prefers AMD CPUs.", "preference")
        ]
    },
    {
        "category": "dance_movement",
        "prompts": [
            "Learn dancing", "Dance styles explained",
            "Dance classes nearby", "Hip hop dance",
            "Improve dance skills", "Dance workout"
        ],
        "highly_relevant": [
            ("Enjoys dancing.", "preference"),
            ("Recently joined dance class.", "task_history"),
            ("Practices salsa.", "preference")
        ],
        "somewhat_relevant": [
            ("Enjoys physical activities.", "preference"),
            ("Likes music.", "preference")
        ],
        "not_relevant": [
            ("Working on ML project.", "project_context"),
            ("Prefers vegetarian food.", "preference")
        ]
    },
    {
        "category": "pets_animals",
        "prompts": [
            "Pet care tips", "Dog training guide",
            "Cat behavior explained", "Choose right pet",
            "Pet health advice", "Pet-friendly activities"
        ],
        "highly_relevant": [
            ("Has pet dog named Max.", "background"),
            ("Recently adopted puppy.", "task_history"),
            ("Looking for vet nearby.", "task_history")
        ],
        "somewhat_relevant": [
            ("Loves animals.", "preference"),
            ("Walks dog daily.", "preference")
        ],
        "not_relevant": [
            ("Working on ML project.", "project_context"),
            ("Prefers AMD CPUs.", "preference")
        ]
    },
    {
        "category": "fashion_style",
        "prompts": [
            "Fashion advice", "Style guide for men",
            "Build wardrobe", "Fashion trends",
            "Dress better tips", "Clothing recommendations"
        ],
        "highly_relevant": [
            ("Interested in fashion.", "preference"),
            ("Recently asked about style tips.", "task_history"),
            ("Wants to improve wardrobe.", "preference")
        ],
        "somewhat_relevant": [
            ("Shops online frequently.", "preference"),
            ("Follows fashion blogs.", "background")
        ],
        "not_relevant": [
            ("Working on ML project.", "project_context"),
            ("Prefers vegetarian food.", "preference")
        ]
    },
    {
        "category": "home_improvement",
        "prompts": [
            "Home improvement ideas", "DIY home projects",
            "Interior design tips", "Renovate room",
            "Home decor suggestions", "Furniture recommendations"
        ],
        "highly_relevant": [
            ("Recently moved to new apartment.", "background"),
            ("Planning room renovation.", "task_history"),
            ("Interested in interior design.", "preference")
        ],
        "somewhat_relevant": [
            ("Enjoys DIY projects.", "preference"),
            ("Values aesthetic living space.", "preference")
        ],
        "not_relevant": [
            ("Working on ML project.", "project_context"),
            ("Prefers AMD CPUs.", "preference")
        ]
    },
    {
        "category": "social_events",
        "prompts": [
            "Plan social gathering", "Party planning ideas",
            "Host dinner party", "Event organization",
            "Social activities ideas", "Meet new people"
        ],
        "highly_relevant": [
            ("Hosting party next week.", "task_history"),
            ("Enjoys social gatherings.", "preference"),
            ("Recently asked about party ideas.", "task_history")
        ],
        "somewhat_relevant": [
            ("Values friendships.", "preference"),
            ("Usually free on weekends.", "device_context")
        ],
        "not_relevant": [
            ("Working on ML project.", "project_context"),
            ("Prefers AMD CPUs.", "preference")
        ]
    },

    # ===== EDUCATION & LEARNING (15 categories) =====
    {
        "category": "online_courses",
        "prompts": [
            "Best online courses", "Learn new skills online",
            "Coursera vs Udemy", "Free online education",
            "Certification courses", "Online learning platforms"
        ],
        "highly_relevant": [
            ("Recently enrolled in online course.", "task_history"),
            ("Learning ML through Coursera.", "background"),
            ("Wants to get certified.", "preference")
        ],
        "somewhat_relevant": [
            ("Enjoys learning.", "preference"),
            ("Studies Computer Engineering.", "background")
        ],
        "not_relevant": [
            ("Prefers vegetarian food.", "preference"),
            ("Enjoys hiking.", "preference")
        ]
    },
    {
        "category": "exam_preparation",
        "prompts": [
            "Exam preparation tips", "Study for competitive exams",
            "Test-taking strategies", "Memorization techniques",
            "Exam anxiety management", "Last-minute revision"
        ],
        "highly_relevant": [
            ("Has exam next week.", "task_history"),
            ("Recently asked about study tips.", "task_history"),
            ("Preparing for certification.", "preference")
        ],
        "somewhat_relevant": [
            ("Studies Computer Engineering.", "background"),
            ("Uses flashcards.", "preference")
        ],
        "not_relevant": [
            ("Prefers vegetarian food.", "preference"),
            ("Enjoys hiking.", "preference")
        ]
    },
    {
        "category": "research_skills",
        "prompts": [
            "Research methodology", "Academic writing guide",
            "Literature review tips", "Research paper structure",
            "Citation styles", "Data analysis for research"
        ],
        "highly_relevant": [
            ("Working on research paper.", "project_context"),
            ("Participates in research groups.", "background"),
            ("Recently asked about citations.", "task_history")
        ],
        "somewhat_relevant": [
            ("Studies at university.", "background"),
            ("Interested in academic career.", "preference")
        ],
        "not_relevant": [
            ("Prefers vegetarian food.", "preference"),
            ("Enjoys gaming.", "preference")
        ]
        },
    {
        "category": "language_learning",
        "prompts": [
            "Learn a new language", "Language learning apps",
            "Duolingo vs Babbel", "Improve language skills",
            "Language immersion techniques", "Learn Spanish fast"
        ],
        "highly_relevant": [
            ("Learning Spanish.", "preference"),
            ("Uses Duolingo daily.", "device_context"),
            ("Recently asked about language learning.", "task_history")
        ],
        "somewhat_relevant": [
            ("Planning trip to Spain.", "task_history"),
            ("Enjoys learning new things.", "preference")
        ],
        "not_relevant": [
            ("Working on ML project.", "project_context"),
            ("Prefers vegetarian food.", "preference")
        ]
    },
    {
        "category": "tutoring_teaching",
        "prompts": [
            "Become a tutor", "Teaching strategies",
            "Online tutoring platforms", "Explain concepts clearly",
            "Tutoring business", "Teaching methods"
        ],
        "highly_relevant": [
            ("Works as part-time tutor.", "background"),
            ("Recently started tutoring.", "task_history"),
            ("Wants to improve teaching skills.", "preference")
        ],
        "somewhat_relevant": [
            ("Good at explaining concepts.", "background"),
            ("Enjoys helping others learn.", "preference")
        ],
        "not_relevant": [
            ("Prefers vegetarian food.", "preference"),
            ("Enjoys hiking.", "preference")
        ]
    },
    {
        "category": "scholarship_funding",
        "prompts": [
            "Find scholarships", "Education funding",
            "Apply for grants", "Student financial aid",
            "Scholarship application tips", "Education loans"
        ],
        "highly_relevant": [
            ("Applying for scholarships.", "task_history"),
            ("Student with limited budget.", "background"),
            ("Recently asked about funding.", "task_history")
        ],
        "somewhat_relevant": [
            ("Studies at university.", "background"),
            ("Planning higher education.", "preference")
        ],
        "not_relevant": [
            ("Working on ML project.", "project_context"),
            ("Prefers vegetarian food.", "preference")
        ]
    },
    {
        "category": "internship_opportunities",
        "prompts": [
            "Find internships", "Internship application tips",
            "Resume for internship", "Best companies for interns",
            "Internship vs job", "Gain work experience"
        ],
        "highly_relevant": [
            ("Looking for summer internship.", "task_history"),
            ("Recently updated resume.", "task_history"),
            ("Wants tech internship.", "preference")
        ],
        "somewhat_relevant": [
            ("Studies Computer Engineering.", "background"),
            ("Has experience in backend development.", "background")
        ],
        "not_relevant": [
            ("Prefers vegetarian food.", "preference"),
            ("Enjoys hiking.", "preference")
        ]
    },
    {
        "category": "academic_writing",
        "prompts": [
            "Improve academic writing", "Write thesis",
            "Research paper tips", "Academic style guide",
            "Avoid plagiarism", "Proofreading techniques"
        ],
        "highly_relevant": [
            ("Writing thesis.", "project_context"),
            ("Recently asked about academic writing.", "task_history"),
            ("Needs to submit paper.", "task_history")
        ],
        "somewhat_relevant": [
            ("Participates in research groups.", "background"),
            ("Studies at university.", "background")
        ],
        "not_relevant": [
            ("Prefers vegetarian food.", "preference"),
            ("Enjoys gaming.", "preference")
        ]
    },
    {
        "category": "group_study",
        "prompts": [
            "Form study group", "Group study benefits",
            "Collaborate on projects", "Study partners",
            "Peer learning", "Academic collaboration"
        ],
        "highly_relevant": [
            ("Looking for study partners.", "task_history"),
            ("Participates in research groups.", "background"),
            ("Recently joined study group.", "task_history")
        ],
        "somewhat_relevant": [
            ("Studies Computer Engineering.", "background"),
            ("Enjoys collaborative work.", "preference")
        ],
        "not_relevant": [
            ("Prefers vegetarian food.", "preference"),
            ("Enjoys hiking.", "preference")
        ]
    },
    {
        "category": "educational_technology",
        "prompts": [
            "EdTech tools", "Digital learning platforms",
            "Educational apps", "Online classroom tools",
            "Learning management systems", "Tech for education"
        ],
        "highly_relevant": [
            ("Uses online learning platforms.", "device_context"),
            ("Recently tried new EdTech tool.", "task_history"),
            ("Interested in educational technology.", "preference")
        ],
        "somewhat_relevant": [
            ("Studies Computer Engineering.", "background"),
            ("Enjoys technology.", "preference")
        ],
        "not_relevant": [
            ("Prefers vegetarian food.", "preference"),
            ("Enjoys hiking.", "preference")
        ]
    },

    # ===== TECHNOLOGY DEVICES (10 categories) =====
   
    {
        "category": "smartwatch_wearables",
        "prompts": [
            "Smartwatch recommendations", "Apple Watch vs Fitbit",
            "Fitness tracker comparison", "Best wearables",
            "Smartwatch for health", "Track fitness with watch"
        ],
        "highly_relevant": [
            ("Uses Fitbit to track steps.", "device_context"),
            ("Recently asked about smartwatches.", "task_history"),
            ("Wants to track fitness better.", "preference")
        ],
        "somewhat_relevant": [
            ("Exercises regularly.", "preference"),
            ("Interested in health tech.", "preference")
        ],
        "not_relevant": [
            ("Working on ML project.", "project_context"),
            ("Prefers vegetarian food.", "preference")
        ]
    },
    {
        "category": "computer_peripherals",
        "prompts": [
            "Best keyboard for coding", "Gaming mouse recommendations",
            "Monitor suggestions", "Mechanical keyboard guide",
            "Ergonomic peripherals", "Webcam for meetings"
        ],
        "highly_relevant": [
            ("Recently bought mechanical keyboard.", "task_history"),
            ("Looking for ergonomic mouse.", "task_history"),
            ("Works 8+ hours at computer.", "device_context")
        ],
        "somewhat_relevant": [
            ("Prefers minimal UI designs.", "preference"),
            ("Values productivity tools.", "preference")
        ],
        "not_relevant": [
            ("Prefers vegetarian food.", "preference"),
            ("Enjoys hiking.", "preference")
        ]
    },
    {
        "category": "home_automation",
        "prompts": [
            "Smart home devices", "Home automation setup",
            "Smart lights recommendations", "Voice assistants",
            "IoT devices", "Automate my home"
        ],
        "highly_relevant": [
            ("Recently bought smart bulbs.", "task_history"),
            ("Interested in home automation.", "preference"),
            ("Uses Alexa at home.", "device_context")
        ],
        "somewhat_relevant": [
            ("Enjoys technology.", "preference"),
            ("Lives in apartment.", "background")
        ],
        "not_relevant": [
            ("Prefers vegetarian food.", "preference"),
            ("Working on ML project.", "project_context")
        ]
    },
    {
        "category": "camera_equipment",
        "prompts": [
            "Camera recommendations", "DSLR vs mirrorless",
            "Photography equipment", "Lens suggestions",
            "Camera for beginners", "Video recording camera"
        ],
        "highly_relevant": [
            ("Enjoys photography.", "preference"),
            ("Recently bought DSLR camera.", "task_history"),
            ("Looking for new lens.", "task_history")
        ],
        "somewhat_relevant": [
            ("Interested in videography.", "preference"),
            ("Shares content online.", "background")
        ],
        "not_relevant": [
            ("Prefers vegetarian food.", "preference"),
            ("Working on ML project.", "project_context")
        ]
    },
    {
        "category": "storage_backup",
        "prompts": [
            "External hard drive recommendations", "Cloud storage comparison",
            "Backup solutions", "NAS setup",
            "Data storage options", "SSD vs HDD"
        ],
        "highly_relevant": [
            ("Stores files in organized folders.", "device_context"),
            ("Recently asked about backups.", "task_history"),
            ("Needs more storage space.", "task_history")
        ],
        "somewhat_relevant": [
            ("Works with large datasets.", "project_context"),
            ("Values data security.", "preference")
        ],
        "not_relevant": [
            ("Prefers vegetarian food.", "preference"),
            ("Enjoys hiking.", "preference")
        ]
    },
    {
        "category": "networking_equipment",
        "prompts": [
            "WiFi router recommendations", "Improve internet speed",
            "Network setup guide", "Mesh WiFi systems",
            "Ethernet vs WiFi", "Home network security"
        ],
        "highly_relevant": [
            ("Recently upgraded router.", "task_history"),
            ("Experiencing slow internet.", "task_history"),
            ("Works from home.", "background")
        ],
        "somewhat_relevant": [
            ("Streams content frequently.", "preference"),
            ("Has multiple devices.", "device_context")
        ],
        "not_relevant": [
            ("Prefers vegetarian food.", "preference"),
            ("Enjoys hiking.", "preference")
        ]
    },
    # ===== MISCELLANEOUS (15 categories) =====
    {
        "category": "weather_queries",
        "prompts": [
            "What's the weather today?", "Weather forecast",
            "Will it rain tomorrow?", "Temperature today",
            "Weather for the week", "Climate information"
        ],
        "highly_relevant": [
            ("Lives in Mumbai.", "background"),
            ("Planning outdoor activity.", "task_history"),
            ("Recently asked about weather.", "task_history")
        ],
        "somewhat_relevant": [
            ("Enjoys hiking.", "preference"),
            ("Usually free on weekends.", "device_context")
        ],
        "not_relevant": [
            ("Working on ML project.", "project_context"),
            ("Prefers AMD CPUs.", "preference")
        ]
    },
    {
        "category": "shopping_recommendations",
        "prompts": [
            "Where to buy online", "Best deals",
            "Shopping recommendations", "Product comparisons",
            "Online vs offline shopping", "Discount codes"
        ],
        "highly_relevant": [
            ("Prefers online shopping.", "preference"),
            ("Recently searched for deals.", "task_history"),
            ("Budget-conscious buyer.", "preference")
        ],
        "somewhat_relevant": [
            ("Shops frequently online.", "preference"),
            ("Uses Amazon Prime.", "device_context")
        ],
        "not_relevant": [
            ("Working on ML project.", "project_context"),
            ("Studies Computer Engineering.", "background")
        ]
    },
    {
        "category": "gift_ideas",
        "prompts": [
            "Gift ideas", "What to gift",
            "Birthday present suggestions", "Thoughtful gifts",
            "Gift for tech person", "Unique gift ideas"
        ],
        "highly_relevant": [
            ("Friend's birthday next week.", "task_history"),
            ("Recently asked about gifts.", "task_history"),
            ("Looking for tech gifts.", "task_history")
        ],
        "somewhat_relevant": [
            ("Enjoys thoughtful gifting.", "preference"),
            ("Shops online.", "preference")
        ],
        "not_relevant": [
            ("Working on ML project.", "project_context"),
            ("Prefers vegetarian food.", "preference")
        ]
    },
    {
        "category": "conversation_casual",
        "prompts": [
            "Tell me a joke", "Random fact",
            "Interesting trivia", "Fun conversation",
            "Chat with me", "Entertainment"
        ],
        "highly_relevant": [
            ("Enjoys casual conversations.", "preference"),
            ("Recently asked for jokes.", "task_history"),
            ("Likes learning random facts.", "preference")
        ],
        "somewhat_relevant": [
            ("Uses assistant for entertainment.", "preference"),
            ("Curious person.", "preference")
        ],
        "not_relevant": [
            ("Working on ML project.", "project_context"),
            ("Prefers vegetarian food.", "preference")
        ]
    },
    {
        "category": "reminders_alarms",
        "prompts": [
            "Set a reminder", "Remind me to",
            "Create alarm", "Schedule reminder",
            "Don't let me forget", "Reminder for later"
        ],
        "highly_relevant": [
            ("Has reminder for project review meeting.", "device_context"),
            ("Recently set reminders.", "task_history"),
            ("Forgets things easily.", "preference")
        ],
        "somewhat_relevant": [
            ("Uses calendar actively.", "device_context"),
            ("Values time management.", "preference")
        ],
        "not_relevant": [
            ("Prefers vegetarian food.", "preference"),
            ("Enjoys hiking.", "preference")
        ]
    },
    {
        "category": "directions_navigation",
        "prompts": [
            "Directions to", "How to get there",
            "Navigate to location", "Route planning",
            "Traffic conditions", "Best route"
        ],
        "highly_relevant": [
            ("Lives in Mumbai.", "background"),
            ("Recently asked for directions.", "task_history"),
            ("Has meeting across town.", "task_history")
        ],
        "somewhat_relevant": [
            ("Commutes daily.", "device_context"),
            ("Uses maps regularly.", "device_context")
        ],
        "not_relevant": [
            ("Working on ML project.", "project_context"),
            ("Prefers AMD CPUs.", "preference")
        ]
    },
    {
        "category": "legal_advice",
        "prompts": [
            "Legal information", "Know my rights",
            "Legal procedures", "Contract help",
            "Legal terminology", "Consumer rights"
        ],
        "highly_relevant": [
            ("Recently asked about legal matters.", "task_history"),
            ("Dealing with contract.", "task_history"),
            ("Needs legal information.", "preference")
        ],
        "somewhat_relevant": [
            ("Values knowing rights.", "preference"),
            ("Careful with documents.", "preference")
        ],
        "not_relevant": [
            ("Working on ML project.", "project_context"),
            ("Prefers vegetarian food.", "preference")
        ]
    },
    {
        "category": "relationship_advice",
        "prompts": [
            "Relationship advice", "Dating tips",
            "Improve communication", "Conflict resolution",
            "Friendship advice", "Social skills"
        ],
        "highly_relevant": [
            ("Recently asked about relationships.", "task_history"),
            ("Dealing with conflict.", "task_history"),
            ("Values healthy relationships.", "preference")
        ],
        "somewhat_relevant": [
            ("Social person.", "preference"),
            ("Values friendships.", "preference")
        ],
        "not_relevant": [
            ("Working on ML project.", "project_context"),
            ("Prefers AMD CPUs.", "preference")
        ]
    },
    {
        "category": "college_admissions",
        "prompts": [
            "College application process", "University selection",
            "Write college essays", "Admission requirements",
            "SAT/GRE preparation", "College interview tips"
        ],
        "highly_relevant": [
            ("Applying to grad schools.", "task_history"),
            ("Recently asked about admissions.", "task_history"),
            ("Preparing for GRE.", "preference")
        ],
        "somewhat_relevant": [
            ("Studies Computer Engineering.", "background"),
            ("Wants higher education.", "preference")
        ],
        "not_relevant": [
            ("Prefers vegetarian food.", "preference"),
            ("Enjoys hiking.", "preference")
        ]
    },
    
    {
        "category": "stem_education",
        "prompts": [
            "STEM career paths", "Science education",
            "Mathematics resources", "Engineering projects",
            "Technology education", "STEM skills"
        ],
        "highly_relevant": [
            ("Studies Computer Engineering.", "background"),
            ("Interested in STEM career.", "preference"),
            ("Recently asked about engineering.", "task_history")
        ],
        "somewhat_relevant": [
            ("Good at mathematics.", "background"),
            ("Enjoys problem-solving.", "preference")
        ],
        "not_relevant": [
            ("Prefers vegetarian food.", "preference"),
            ("Enjoys hiking.", "preference")
        ]
    },
    {
        "category": "educational_resources",
        "prompts": [
            "Best learning resources", "Educational websites",
            "Study materials recommendations", "Free textbooks",
            "Educational YouTube channels", "Learning tools"
        ],
        "highly_relevant": [
            ("Looking for study materials.", "task_history"),
            ("Recently asked about resources.", "task_history"),
            ("Studies Computer Engineering.", "background")
        ],
        "somewhat_relevant": [
            ("Enjoys learning.", "preference"),
            ("Takes online courses.", "background")
        ],
        "not_relevant": [
            ("Prefers vegetarian food.", "preference"),
            ("Enjoys hiking.", "preference")
        ]
    },
    
    {
        "category": "graduation_planning",
        "prompts": [
            "After graduation plans", "Career after college",
            "Graduate school vs job", "Post-graduation options",
            "Alumni networking", "Graduation preparation"
        ],
        "highly_relevant": [
            ("Graduating next year.", "background"),
            ("Recently asked about post-grad.", "task_history"),
            ("Planning career path.", "preference")
        ],
        "somewhat_relevant": [
            ("Studies Computer Engineering.", "background"),
            ("Interested in job market.", "preference")
        ],
        "not_relevant": [
            ("Prefers vegetarian food.", "preference"),
            ("Enjoys hiking.", "preference")
        ]
    },
    {
        "category": "lifelong_learning",
        "prompts": [
            "Continuous learning", "Learn throughout life",
            "Skill development after 30", "Never stop learning",
            "Adult education", "Personal growth"
        ],
        "highly_relevant": [
            ("Values continuous learning.", "preference"),
            ("Recently asked about skill development.", "task_history"),
            ("Takes courses regularly.", "background")
        ],
        "somewhat_relevant": [
            ("Enjoys learning new things.", "preference"),
            ("Reads educational content.", "preference")
        ],
        "not_relevant": [
            ("Prefers vegetarian food.", "preference"),
            ("Enjoys hiking.", "preference")
        ]
    },

    # ===== TECHNOLOGY DEVICES (10 categories) =====
    {
        "category": "smartphone_selection",
        "prompts": [
            "Suggest a smartphone to buy", "Which phone is best for me?",
            "Recommend a mobile device", "Help me choose a new phone",
            "iPhone vs Android", "Best budget phone"
        ],
        "highly_relevant": [
            ("Prefers high refresh-rate displays.", "preference"),
            ("Uses dark mode on most apps.", "preference"),
            ("Syncs tasks across laptop and phone.", "device_context"),
            ("Recently asked about phones.", "task_history")
        ],
        "somewhat_relevant": [
            ("Prefers minimal UI designs.", "preference"),
            ("Budget is around $800 for phone.", "preference")
        ],
        "not_relevant": [
            ("Prefers vegetarian food.", "preference"),
            ("Working on AWAF dashboard backend.", "project_context")
        ]
    },
    {
        "category": "tablet_devices",
        "prompts": [
            "iPad vs Android tablet", "Best tablet for students",
            "Tablet recommendations", "Drawing tablet",
            "Tablet for reading", "Productivity tablet"
        ],
        "highly_relevant": [
            ("Looking for tablet for note-taking.", "task_history"),
            ("Recently asked about tablets.", "task_history"),
            ("Prefers iPad for creativity.", "preference")
        ],
        "somewhat_relevant": [
            ("Studies at university.", "background"),
            ("Enjoys digital art.", "preference")
        ],
        "not_relevant": [
            ("Prefers vegetarian food.", "preference"),
            ("Enjoys hiking.", "preference")
        ]
    },

    {
        "category": "audio_devices",
        "prompts": [
            "Headphones recommendations", "Best earbuds",
            "Noise-canceling headphones", "Audio quality comparison",
            "Wireless earbuds", "Gaming headset"
        ],
        "highly_relevant": [
            ("Recently bought AirPods.", "task_history"),
            ("Prefers noise-canceling headphones.", "preference"),
            ("Listens to music daily.", "preference")
        ],
        "somewhat_relevant": [
            ("Works in noisy environment.", "device_context"),
            ("Enjoys high-quality audio.", "preference")
        ],
        "not_relevant": [
            ("Prefers vegetarian food.", "preference"),
            ("Working on ML project.", "project_context")
        ]
    },
    {
        "category": "charging_power",
        "prompts": [
            "Power bank recommendations", "Fast charging guide",
            "Cable management", "Wireless charging",
            "Battery life tips", "Charging accessories"
        ],
        "highly_relevant": [
            ("Recently bought power bank.", "task_history"),
            ("Phone battery drains quickly.", "task_history"),
            ("Travels frequently.", "preference")
        ],
        "somewhat_relevant": [
            ("Uses multiple devices.", "device_context"),
            ("Values convenience.", "preference")
        ],
        "not_relevant": [
            ("Prefers vegetarian food.", "preference"),
            ("Working on ML project.", "project_context")
        ]
    },

    # ===== MISCELLANEOUS (15 categories) =====
    {
        "category": "local_recommendations",
        "prompts": [
            "Best places nearby", "Local attractions",
            "Things to do in my city", "Nearby restaurants",
            "Local events", "Explore my area"
        ],
        "highly_relevant": [
            ("Lives in Mumbai.", "background"),
            ("Recently asked about local places.", "task_history"),
            ("Usually free on weekends.", "device_context")
        ],
        "somewhat_relevant": [
            ("Enjoys exploring.", "preference"),
            ("Likes trying new restaurants.", "preference")
        ],
        "not_relevant": [
            ("Working on ML project.", "project_context"),
            ("Prefers AMD CPUs.", "preference")
        ]
    },
    {
        "category": "news_current_events",
        "prompts": [
            "Latest news", "Current events",
            "Tech news today", "What's happening",
            "News summary", "Breaking news"
        ],
        "highly_relevant": [
            ("Reads tech news daily.", "preference"),
            ("Recently asked about current events.", "task_history"),
            ("Interested in technology news.", "preference")
        ],
        "somewhat_relevant": [
            ("Stays informed.", "preference"),
            ("Uses news apps.", "device_context")
        ],
        "not_relevant": [
            ("Prefers vegetarian food.", "preference"),
            ("Enjoys hiking.", "preference")
        ]
    },
    {
        "category": "motivational_quotes",
        "prompts": [
            "Motivational quotes", "Inspire me",
            "Daily motivation", "Positive affirmations",
            "Encouraging words", "Motivational content"
        ],
        "highly_relevant": [
            ("Enjoys motivational content.", "preference"),
            ("Recently feeling demotivated.", "task_history"),
            ("Values positive mindset.", "preference")
        ],
        "somewhat_relevant": [
            ("Practices gratitude.", "preference"),
            ("Journals daily.", "preference")
        ],
        "not_relevant": [
            ("Working on ML project.", "project_context"),
            ("Prefers AMD CPUs.", "preference")
        ]
    },
    {
        "category": "definitions_explanations",
        "prompts": [
            "Define this term", "Explain concept",
            "What does this mean?", "Simple explanation",
            "ELI5", "Break down this topic"
        ],
        "highly_relevant": [
            ("Recently asked for explanations.", "task_history"),
            ("Learning new concepts.", "background"),
            ("Values clear understanding.", "preference")
        ],
        "somewhat_relevant": [
            ("Studies Computer Engineering.", "background"),
            ("Curious learner.", "preference")
        ],
        "not_relevant": [
            ("Prefers vegetarian food.", "preference"),
            ("Enjoys hiking.", "preference")
        ]
    },
    {
        "category": "calculations_conversions",
        "prompts": [
            "Calculate this", "Unit conversion",
            "Currency exchange", "Math help",
            "Convert units", "Quick calculation"
        ],
        "highly_relevant": [
            ("Recently asked for calculations.", "task_history"),
            ("Uses device for quick math.", "device_context"),
            ("Good at mathematics.", "background")
        ],
        "somewhat_relevant": [
            ("Studies engineering.", "background"),
            ("Works with numbers.", "project_context")
        ],
        "not_relevant": [
            ("Prefers vegetarian food.", "preference"),
            ("Enjoys hiking.", "preference")
        ]
    },
    {
        "category": "health_symptoms",
        "prompts": [
            "Health symptoms check", "What causes",
            "Medical information", "First aid",
            "Health advice", "Symptom checker"
        ],
        "highly_relevant": [
            ("Recently asked about health.", "task_history"),
            ("Experiencing symptoms.", "task_history"),
            ("Values health information.", "preference")
        ],
        "somewhat_relevant": [
            ("Health-conscious.", "preference"),
            ("Exercises regularly.", "preference")
        ],
        "not_relevant": [
            ("Working on ML project.", "project_context"),
            ("Prefers AMD CPUs.", "preference")
        ]
    },
    {
        "category": "environmental_sustainability",
        "prompts": [
            "Environmental tips", "Reduce carbon footprint",
            "Sustainable living", "Eco-friendly practices",
            "Climate action", "Green lifestyle"
        ],
        "highly_relevant": [
            ("Values sustainability.", "preference"),
            ("Recently asked about eco-living.", "task_history"),
            ("Wants to reduce waste.", "preference")
        ],
        "somewhat_relevant": [
            ("Environmentally conscious.", "preference"),
            ("Recycles regularly.", "preference")
        ],
        "not_relevant": [
            ("Working on ML project.", "project_context"),
            ("Prefers AMD CPUs.", "preference")
        ]
    }
    
]