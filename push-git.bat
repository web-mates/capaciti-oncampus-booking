echo // First delete the hidden .git folder before launching this batch file
git init
git add .
git commit -m "first commit"
git remote add origin https://github.com/web-mates/capaciti-oncampus-booking.git
git push origin master