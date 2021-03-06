# Hosting telegram bot on [Heroku](https://heroku.com) for free.
Easy way to host your python telegram bot on Heroku

## Deploying via [Heroku Dashboard](https://dashboard.heroku.com) (GUI)
1. [Fork](https://github.com/Kylmakalle/heroku-telegram-bot/fork) this repo to your account. 
2. [Edit files](https://github.com/Kylmakalle/heroku-telegram-bot#edit-files)
3. Go to [Dashboard](https://dashboard.heroku.com), login, Press _New_ and choose _Create new app._
4. Fill in an _App Name_ and choose _Runtime Region._
5. Connect your GitHub repo at _Deploy_ page.
6. Setup **Automatics deploys** _(Optionaly)._
7. _Deploy a GitHub branch._
8. Then go to a _Settings_ page, click _Reveal Config Vars_ and then add your own, for example:
![Config Vars](http://i.imgur.com/C3cmphh.png)
9. **Finally**, go to the _Resources_ page.
    1. Install _Heroku Redis_ add-on _(Optionaly)_
    2. Press on a small pen button, move slider and then click _Confirm_, that will start bot dyno.
    3. Simply move slider back if you need to stop bot dyno, remember to click _Confirm_.
    4. If for some reason it’s not working, check the logs here 
    
    ![Logs](http://i.imgur.com/rIHU6zF.png)

### More about
- https://devcenter.heroku.com/articles/dynos
- https://devcenter.heroku.com/articles/config-vars
- https://devcenter.heroku.com/articles/heroku-redis
- https://devcenter.heroku.com/articles/error-codes

Thanks to [Roman Zaynetdinov](https://github.com/zaynetro) for awesome and easy CLI guide.
