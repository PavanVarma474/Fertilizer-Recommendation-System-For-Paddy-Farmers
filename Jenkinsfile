pipeline {
    agent any

    environment {
        VIRTUAL_ENV = "${WORKSPACE}/venv"
        PIP_CACHE_DIR = "${WORKSPACE}/.pip_cache"
    }

    stages {
        stage('Checkout') {
            steps {
                git 'https://github.com/PavanVarma474/Fertilizer-Recommendation-System-For-Paddy-Farmers'
            }
        }

        stage('Setup Python') {
            steps {
                sh '''
                python3 -m venv ${VIRTUAL_ENV}
                . ${VIRTUAL_ENV}/bin/activate
                '''
            }
        }

        stage('Install Dependencies') {
            steps {
                sh '''
                . ${VIRTUAL_ENV}/bin/activate
                pip install --cache-dir=${PIP_CACHE_DIR} -r requirements.txt
                '''
            }
        }

        stage('Run Tests') {
            steps {
                sh '''
                . ${VIRTUAL_ENV}/bin/activate
                pytest
                '''
            }
        }

        stage('Run Application') {
            steps {
                sh '''
                . ${VIRTUAL_ENV}/bin/activate
                export FLASK_APP=app.py
                flask run --host=0.0.0.0
                '''
            }
        }
    }

    post {
        success {
            echo 'Pipeline completed successfully!'
        }
        failure {
            echo 'Pipeline failed!'
        }
    }
}
