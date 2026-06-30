pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                echo 'Getting project code...'
            }
        }

        stage('Check Files') {
            steps {
                sh '''
                pwd
                ls -la
                '''
            }
        }

        stage('Run App Test') {
            steps {
                sh '''
                python3 -m py_compile app.py || python -m py_compile app.py
                echo "app.py syntax is OK"
                '''
            }
        }

        stage('Success') {
            steps {
                echo 'Jenkins pipeline completed successfully'
            }
        }
    }
}