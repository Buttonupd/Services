#!groovy

node {

    try {
        stage 'Checkout'
            checkout scm
        stage 'Test'
            sh 'virtualenv env -p python3.9'
            sh '. env/bin/activate'
            sh 'env/bin/pip install -r requirements.txt'
            sh 'env/bin/python3 manage.py test.py'
        stage 'Deploy'
            sh './deployment/deploy_prod.sh'

        stage 'Publish results'
            
    }

    catch (err) {
       

        throw err
    }

}
