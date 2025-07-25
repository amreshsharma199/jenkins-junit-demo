pipeline {
    agent { label 'jenkinsslave' }

    stages {
        stage('Test in Docker') {
            steps {
                script {
                    def myImage = docker.build("python-test")
                    myImage.inside {
                        sh 'python3 -m pytest test_app.py --junitxml=results.xml'
                    }
                }
            }
        }

        stage('Publish Report') {
            steps {
                junit 'results.xml'
            }
        }
    }
}
// pipeline {
//     agent { label 'jenkinsslave' }

//     stages {
//         stage('Clone') {
//             steps {
//                 git branch: 'main', url: 'https://github.com/amreshsharma199/jenkins-junit-demo.git'
//             }
//         }

//         stage('Test in Docker') {
//             steps {
//                 script {
//                     docker.build('my-python-app').inside {
//                         sh 'pytest test_app.py'
//                     }
//                 }
//             }
//         }
//     }
// }
