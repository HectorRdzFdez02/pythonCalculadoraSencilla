pipeline {
    agent any

    triggers {
        githubPush()
    }

    stages {

        stage('Checkout') {
            steps {
                git url: 'https://github.com/HectorRdzFdez02/pythonCalculadoraSencilla.git', branch: 'main'
            }
        }

        stage('Run program') {
            steps {
                sh 'python3 calculadora.py 3 4'
            }
        }

        stage('Unit tests') {
            steps {
                sh 'python3 test_Calculadora.py'
            }
        }
    }
}
