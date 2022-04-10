class Dict(dict):
    def __init__(self,*args,**kwargs):
        super().__init__(*args,**kwargs)
        self.__dict__=self
    def update(self,args):
        super().update(args)
        self.__dict__=self
    def repr_(self,buff=''):
        string=""
        for k,v in self.items():
            string+=buff+f"-{k}:"
            if isinstance(v,self.__class__):
                string+="\n"+v.repr_(buff=buff+"  ")
            elif (isinstance(v,list) or \
                  isinstance(v,tuple)):
                string+=f"\n"+buff+"  "+str(v[0])+f",...*{len(v)}\n" 
            else:
                string+=f"{v}\n"
        if buff=='':
            print(string)
        else:
            return string


registered=Dict(
    models=Dict(),
    datasets=Dict(),
    losses=Dict(),)
def register(dictionary):
    def decorator(cls):
        dictionary.update({str(cls)[17:-2]:cls})
        return cls
    return decorator

@register(registered.models)
class XXOONetwork:
    def __init__(self,a):
        self.a=a