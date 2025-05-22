pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                git url: 'https://github.com/Andynator3/CI_RPG.git', branch: 'main', credentialsId: 'jenkins-example-github'
            }
        }
        stage('Install Python & pip') {
            steps {
                sh '''
                python3 --version || sudo apt-get install python3 -y
                python3 -m pip install --upgrade pip
                '''
            }
        }
        stage('Install dependencies') {
            steps {
                sh '''
                if [ -f requirements.txt ]; then
                    pip3 install -r requirements.txt
                fi
                '''
            }
        }
        stage('Run tests') {
            steps {
                sh 'python3 -m unittest discover'
            }
        }
    }
}
