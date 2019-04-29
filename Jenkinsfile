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
        sh 'pip install -p requirements.txt'
      }
    }
  
    stage('QualityTest') { 
            steps {
		    sh '(/var/jenkins_home/workspace/LSR_Project_qdl/sonar-scanner-3.3.0.1492-linux/bin/sonar-scanner  -Dsonar.projectKey=Versusfinder   -Dsonar.organization=skogarmadr-github   -Dsonar.sources=.   -Dsonar.host.url=https://sonarcloud.io -Dsonar.login=c21936d712b162805304fa999c443ef933b4b246)'
	    }
    }
  }
}