# oauth
基于 OAuth 协议的第三方登录

学习了一下 OAuth 协议，具体过程为：

1. 从 Github 申请 Client Id 和  Client Secret

2. 用户点击通过 Github 登录，跳转到 Giihub 授权页面

3. 用户确认授权后，Github 确认 Client Id 后跳转到 redirect_uri，附带一个 Code

4. 我的网站后端将这个 code 和 Client Secret 发送给 Github 

5. Github 确认 code 和 Client Secret 后返回 access token

6. 我的网站就可以通过 access token 到 Github 获取相应的用户信息