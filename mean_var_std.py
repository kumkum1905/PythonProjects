import numpy as np
def calculate(list):
    if len(list)!=9:
        raise ValueError("list must contain 9 elements")
    else:
        arr=np.array(list)
        arr=arr.reshape(3,3)
        mean=[np.mean(arr,axis=0).tolist(),np.mean(arr,axis=1).tolist(),np.mean(arr).tolist()]   
        vari=[np.var(arr,axis=0).tolist(),np.var(arr,axis=1).tolist(),np.var(arr).tolist()]
        sd=[np.std(arr,axis=0).tolist(),np.std(arr,axis=1).tolist(),np.std(arr).tolist()]
        max=[np.max(arr,axis=0).tolist(),np.max(arr,axis=1).tolist(),np.max(arr).tolist()]
        min=[np.min(arr,axis=0).tolist(),np.min(arr,axis=1).tolist(),np.min(arr).tolist()]
        sum=[np.sum(arr,axis=0).tolist(),np.sum(arr,axis=1).tolist(),np.sum(arr).tolist()]
        d={'mean':mean,'variance':vari,'standard deviation':sd,'maximum':max,'minimum':min,'sum':sum}
        return d 
print(calculate([0,1,2,3,4,5,6,7,8]))


