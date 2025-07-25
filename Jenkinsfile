pipeline {
    agent { label 'jenkinsslave' }

    stages {
        stage('Clone') {
            steps {
                git branch: 'main', url: 'https://github.com/amreshsharma199/jenkins-junit-demo.git'
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
