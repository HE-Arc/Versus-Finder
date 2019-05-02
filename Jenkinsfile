pipeline {
  agent any

  stages {
    stage('Build') {
             agent {
              docker {
               image 'maven:3-alpine'
              }
            }
            steps {
			    sh '(mvn clean package)'
			    stash name: "app", includes: "**"
            }
    }


    stage('Install dependencies') {
      steps {
        sh 'pip install -r source/requirements.txt'
      }
    }

    stage('QualityTest') { 
            steps {
		    sh '($(pwd)/source/sonar-scanner-3.3.0.1492-linux/bin/sonar-scanner  -Dsonar.projectKey=Versusfinder   -Dsonar.organization=skogarmadr-github   -Dsonar.sources=./source -Dsonar.exclusions=./versusfindertest  -Dsonar.host.url=https://sonarcloud.io -Dsonar.login=c21936d712b162805304fa999c443ef933b4b246)'
	    }
    } 
    
    stage('IntegrationTest') {
             agent {
              docker {
               image 'lucienmoor/katalon-for-jenkins:latest'
               args '-p 9999:9090'  
              }
            }
            steps {
			    sh 'chmod +x ./source/runTest.sh'
			    sh './source/runTest.sh'
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