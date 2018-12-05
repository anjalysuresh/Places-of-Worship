node {
  // Mark the code checkout 'stage'....
    
   
    dir('Content_Tools') {
        git url: 'https://github.com/anjalysuresh/Community-Content-Tools.git'
    }
    dir('Eventlogs') {
        git url: 'https://github.com/anjalysuresh/Collaboration-System-Event-Logs.git'
    }
  dir('Recommendation') {
        git url: 'https://github.com/anjalysuresh/Community-Recommendation.git'
    }
  
  
  
  
  stage ('Stage Checkout'){

  // Checkout code from repository and update any submodule
    
    
  checkout scm
  checkout scm
  checkout scm  
  
   checkout ([
            $class: 'GitSCM',
            branches: [[name: '*/notifications']],
            doGenerateSubmoduleConfigurations: false,
            extensions: [[$class: 'RelativeTargetDirectory',
            relativeTargetDir: 'Notification_Selenium']],
            submoduleCfg: [],
  userRemoteConfigs: [[url: 'https://github.com/anjalysuresh/Collaboration-System-Selenium.git']]])
     
     
     
     
    
    
  } 
 // sh 'git submodule update --init'  

  //stage 'Stage Build'
  
  stage('build') {
            
                echo 'Building..'
                
                sh "./collab.sh"
              
                sh "./Content_Tools/h5p_etherpad.sh"

                sh "./Eventlogs/eventlog.sh"

                sh "./Recommendation/recommendation.sh" 
    
                sh "./community.sh"
            
        } 
    
   stage('test')
     {
      sh "./test.sh"  
      sh "./selen.sh"
     }
   
    
  
  //branch name from Jenkins environment variables
  // echo "My branch is: ${env.BRANCH_NAME}"

//  def flavor = flavor(env.BRANCH_NAME)
 // echo "Building flavor ${flavor}"

  //build your gradle flavor, passes the current build number as a parameter to gradle
//  sh "./gradlew clean assemble${flavor}Debug -PBUILD_NUMBER=${env.BUILD_NUMBER}"

//  stage 'Stage Archive'
  //tell Jenkins to archive the apks
//  archiveArtifacts artifacts: 'app/build/outputs/apk/*.apk', fingerprint: true

//  stage 'Stage Upload To Fabric'
 // sh "./gradlew crashlyticsUploadDistribution${flavor}Debug  -PBUILD_NUMBER=${env.BUILD_NUMBER}"
  
}
