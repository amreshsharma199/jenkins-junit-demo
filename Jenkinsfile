pipeline {
    agent any

    stages {
        stage('Clone') {
            steps {
                git 'https://github.com/amreshsharma199/python-docker-test-demo.git'
            }
        }

        stage('Test in Docker') {
            steps {
                script {
                    docker.build('my-python-app').inside {
                        sh 'pytest test_app.py'
                    }
                }
            }
        }
    }
}
