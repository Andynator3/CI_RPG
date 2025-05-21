pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                // Clone le dépôt depuis GitHub
                git url: 'https://github.com/Andynator3/CI_RPG.git', branch: 'principal', credentialsId: 'github-token'
            }
        }
        stage('Install Python & pip') {
            steps {
                // Vérifie et installe Python/pip si besoin
                sh '''
                python3 --version || brew install python3
                python3 -m pip install --upgrade pip
                '''
            }
        }
        stage('Install dependencies') {
            steps {
                // Installe les dépendances si requirements.txt existe
                sh '''
                if [ -f requirements.txt ]; then
                    pip3 install -r requirements.txt
                fi
                '''
            }
        }
        stage('Run tests') {
            steps {
                // Lance tous les tests unitaires Python
                sh 'python3 -m unittest discover'
            }
        }
    }
}
