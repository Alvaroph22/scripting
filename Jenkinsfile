pipeline {
    agent any

    stages {
        stage('Verify Tools') {
            steps {
                bat 'python --version'
                bat 'pip --version'
            }
        }
        stage('Clone Repository') {
            steps {
                git branch: 'main', url: 'https://github.com/Alvaroph22/scripting.git'
            }
        }
        stage('Install Dependencies') {
            steps {
                // Install Python dependencies
                bat 'pip install -r requirements.txt'
            }
        }
        stage('Compile Application') {
            steps {
                // Run the Python application
                bat 'python main.py'
            }
        }
        stage('Run Tests') {
            steps {
                // Run pytest
                bat 'pytest'
            }
        }
    }
}
