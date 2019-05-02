pipeline {
  agent {
    docker { image 'python:3.7.1' }
  }

  stages {
    stage ('build') {
      steps {
        sh 'python --version'
      }
    }

    stage('Install dependencies') {
      steps {
        sh 'pip install -r requirements.txt'
      }
    }

    
    
    stage('IntegrationTest') {
             agent {
              docker {
               image 'lucienmoor/katalon-for-jenkins:latest'
               args '-p 8888:8080'
              }
            }
            steps {
                unstash "app"
                sh 'java -jar target/SMF-0.0.1-SNAPSHOT.jar >/dev/null 2>&1 &'
                sh 'sleep 30'
			    sh 'chmod +x ./runTest.sh'
			    sh './runTest.sh'
			    cleanWs()
            }
            post {
                always {
                    echo 'always clean up'
                    deleteDir()
                }
            }
        }

  }
}