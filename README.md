# Wine quality detector with MLOps

A wine quality detector as complete machine learning feature with operations (MLOps) | using ML Flow | HTML, CSS | Render ! 


## Full-Product Structure

liqor-quality-app/
├── .github/workflows/       # CI/CD pipelines (GitHub Actions)
├── backend/                 # FastAPI application
│   ├── app/
│   │   ├── api/             # API routes (v1/v2)
│   │   ├── core/            # Config, security, JWT
│   │   ├── crud/            # Database logic
│   │   ├── models/          # SQL database models
│   │   ├── schemas/         # Pydantic request/response models
│   │   ├── services/        # Business logic
│   │   └── main.py          # App entry point
│   ├── tests/               # Backend unit/integration tests
│   ├── Dockerfile           # Backend containerization
│   └── requirements.txt     # Python dependencies
├── frontend/                # React application (Vite/TS)
│   ├── src/
│   │   ├── components/      # Reusable UI elements
│   │   ├── hooks/           # Custom React hooks
│   │   ├── services/        # API client/Axios calls to FastAPI
│   │   └── App.tsx          # Main React component
│   ├── Dockerfile           # Frontend containerization
│   └── package.json         # Frontend dependencies
├── wine-quality-detector/   # Specifically, this MLOps specific directory
│   ├── research/            # Jupyter Notebook experimental EDA and modeling
│   ├── src/                 # Production-grade ML scripts
│   │   ├── components/      # Data ingestion and cleaning
│   │   ├── config/          # Configaration file
│   │   └── pipeline/        # ML pipeline followed by components
│   ├── logs/                # Logging files (for production: logging, exception handling, and src ->wqProject -> utils (common functions))
│   ├── params.yaml/         # Parameters for tuning ML model performance
│   └── app.py/              # integrated to UI and main.py 
├── docker-compose.yml       # Orchestrates all services for dev/prod
├── .env                     # Global environment variables
└── README.md


## Steps of implementation

1. Created folder structure in ```template.py```

2. Listed dependencies in ```requirements.txt```

3. Wrote ```setup.py``` which should be picked by ```-e .``` from requirements.txt that allows the project folder to behave like a package

4. Logging, Exception, Utilities

- added logger in ```src/__init__.py```

- for all common functionalities, created ```utils/common.py```

## 5. Workflows

i.  update config.yaml
ii. update schema.yaml
iii.update params.yaml
iv. update the entity
v.  update the configaration manager in src config
vi. update the ```components```
vii. update the ```pipeline```
viii. update the ```main.py```
ix. update the app.py 

## 5.1