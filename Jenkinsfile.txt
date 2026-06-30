pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                echo 'Getting project code...'
            }
        }

        stage('Install Dependencies') {
            steps {
                bat 'pip install -r requirements.txt'
            }
        }

        stage('Run App Test') {
            steps {
                bat 'python -m py_compile app.py'
            }
        }

        stage('Docker Compose Build') {
            steps {
                bat 'docker compose build'
            }
        }

        stage('Deploy Containers') {
            steps {
                bat 'docker compose up -d'
            }
        }

        stage('Verify App') {
            steps {
                bat 'curl http://localhost:5000'
            }
        }
    }
}