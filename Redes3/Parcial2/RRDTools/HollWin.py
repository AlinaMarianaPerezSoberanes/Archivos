def exponencial_simple(series,alpha):
    result=[series[0]]#Pirmer valor de la serie
    for n in range(1,len(series)):
        result.append(alpha*series[n]+(1-alpha)* result[n-1])
    return result
def exponencial_doble(series,alpha,beta):
    result=[series[0]]
    for n in range(1,len(series)+1):
        if n==1:
            level,trend=series[0],series[1]-series[0]
        if n>=len(series):
            value=result[-1]
        else:
            value=series[n]
            last_level,level=level,alpha*value+(1-alpha)*(level+trend)
            trend=beta*(level-last_level)+(1-beta)* trend
            result.append(level+trend)
    return result

def triple_exponencial(series,slen,alpha,beta,gamma,n_preds):
    result=[]
    seasonals=initial_seasonal_components(series,slen)
    for i in range(len(series)+n_preds):
        if i==0:
            smooth=series[0]
            trend=initial_trend(series,slen)
            result.append(series[0])
            continue
        if i>= len(series):
            m=i-len(series)+1
            result.append((smooth+m*trend)+seasonals[i%slen])
        else:
            val=series[i]
            last_smooth,smooth=smooth, alpha*(val-seasonals[i%slen])+(1-alpha)*smooth
            trend=beta*(smooth-last_smooth)+(1-beta)* trend
            seasonals[i%slen]= gamma*(val-smooth)+(1-gamma)*seasonals[i%slen]
            result.append(smooth+trend+seasonals[i%slen])
    return result


series=[3,3.7,4.53,5.377,6.093,6.43537,6.991833]
series2=[]
series2=exponencial_simple(series,0.1)
series3=exponencial_doble(series2,0.9,0.9)
print(series3)