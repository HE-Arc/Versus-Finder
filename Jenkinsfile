pipeline {
    agent { docker { image 'python:3.7.3' } }
    stages {
        stage('Install dependencies') {
                steps {
                    sh 'pip install -r requirements.txt'
                }
            }
            
            stage('build') {
                steps {
                    sh 'python --version'
                }
            }
    }
    }
}
}