pipeline {
    agent any

    stages {
        stage('Build') {
            steps {
                script {
                    // Build the Docker image
                    sh 'docker-compose build color-changer'
                }
            }
        }

        stage('Test') {
            steps {
                script {
                    // Run tests or validate the application
                    // For example, run a curl command to check if the app responds
                    def response = sh(script: 'curl -s -o /dev/null -w "%{http_code}" http://localhost:8000', returnStdout: true).trim()
                    if (response != '200') {
                        error "Application did not respond with HTTP 200"
                    }
                }
            }
        }

        stage('Deploy') {
            steps {
                script {
                    // You can add deployment steps here if needed
                    echo 'Deployment steps go here'
                }
            }
        }
    }
    
    post {
        always {
            // Clean up or notifications
            echo 'Cleaning up...'
        }
    }
}
