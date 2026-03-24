pipeline {
    agent any

    environment {
        DOCKERHUB_USERNAME = "gaurisathya"
        ROLL_NUMBER = "2023bcs0034"

        IMAGE_FRONTEND = "${DOCKERHUB_USERNAME}/${ROLL_NUMBER}_frontend"
        IMAGE_BACKEND  = "${DOCKERHUB_USERNAME}/${ROLL_NUMBER}_backend"
    }

    stages {

        stage('Build Docker Images') {
            steps {
                script {
                    sh "docker build -t $IMAGE_FRONTEND ./frontend"
                    sh "docker build -t $IMAGE_BACKEND ./backend"
                }
            }
        }

        stage('Login to Docker Hub') {
            steps {
                withCredentials([usernamePassword(credentialsId: 'dockerhub-creds',
                                 usernameVariable: 'USER',
                                 passwordVariable: 'PASS')]) {
                    sh "echo $PASS | docker login -u $USER --password-stdin"
                }
            }
        }

        stage('Push Docker Images') {
            steps {
                script {
                    sh "docker push $IMAGE_FRONTEND"
                    sh "docker push $IMAGE_BACKEND"
                }
            }
        }
    }
}