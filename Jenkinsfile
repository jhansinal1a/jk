pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                echo 'Code pulled from GitHub successfully'
            }
        }

        stage('Check Files') {
            steps {
                sh '''
                pwd
                ls -la

                if [ -f app.py ]; then
                    echo "app.py found"
                else
                    echo "app.py not found"
                    exit 1
                fi
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