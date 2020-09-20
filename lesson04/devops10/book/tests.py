from django.test import TestCase

# Create your tests here.



import casbin


e = casbin.Enforcer("./keymatch_model.conf", "./keymatch_policy.csv")