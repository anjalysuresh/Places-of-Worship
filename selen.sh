
#!/bin/bash
cd Notification_Selenium
cd Notification-system-Testing-using-selenium-master
mkdir -p ./allure-results



 # The sequence of runnning the following test cases is important
 python3 -m virtualenv venv
 . venv/bin/activate
 pip3 install python-decouple

Xvfb :10 -ac &
export DISPLAY=:10

echo '### Creating allure results directory ###'

pip3 install pytest
pip3 install selenium==3.13
 

 python3 create_users.py
 python3 create_community.py
 python3 assign_role_to_users.py
 python3 create_article.py
 python3 create_group.py
 python3 users_joining_group.py
 
 python3 create_article_in_group.py
  echo "ENVIRONMENT SUCCESSFULLY CREATED!" 
 
  python3 Feed_for_draft_to_visible.py	#error on trying to make visible
  python3 Notification_for_editing_the_article.py
  python3 Feeds_and_notification_for_visible_to_publishable.py
  python3 Feeds_and_notification_for_publishable_to_publisher.py
 
  python3 Group_article_draft_to_private.py
  python3 Group_edit_private_articles_.py
  python3 Group_article_private_to_visible.py
  python3 Group_article_visible_rejected_to_private.py #Article goes to private state after rejection
  python3 Group_article_private_to_visible.py
  python3 Group_edit_the_visible_article.py
  python3 Group_article_visible_to_publish.py

  python3 Removing_users_in_the_group.py
  python3 users_joining_group.py

  python3 Group_role_change.py
 
  python3 Subscribe_the_community.py
  python3 Unsubscribe_the_community.py

  python3 Role_to_role_change.py
  python3 Remove_the_users_of_different_roles.py
  
  deactivate
