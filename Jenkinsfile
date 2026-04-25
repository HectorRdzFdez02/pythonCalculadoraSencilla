pipeline {
    agent any

    triggers {
        githubPush()
    }

    stages {

        stage('Run program') {
            steps {
                sh 'python3 calculadora.py 3 4'
            }
        }

        stage('Unit tests') {
            steps {
                sh 'python3 test_calculadora.py'
            }
        }
    }
}
