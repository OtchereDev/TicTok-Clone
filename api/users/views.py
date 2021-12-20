from django.shortcuts import render

class UserSignUpView():
    def post(self,request,*args,**kwargs):
        pass

class UserLoginView():
    def post(self,request,*args,**kwargs):
        pass

class UserForgotPassword():
    def post(self,request,*args,**kwargs):
        pass

class UserVerifyForgotPassword():
    def post(self,request,*args,**kwargs):
        pass

class UserChangePassword():
    def post(self,request,*args,**kwargs):
        pass

class UserGetProfile():
    def post(self,request,*args,**kwargs):
        pass

class UserResendActivation():
    def post(self,request,*args,**kwargs):
        pass

class UserDeletion():
    def delete(self,request,*args,**kwargs):
        pass
