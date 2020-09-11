pvec=seq(0,1,by=0.2)
pn=length(pvec)
pvec
n=1000
res=matrix(data=NA, ncol=pn, nrow=n)
Y=rep(0,n)
for (i in (1:pn)){
  p=pvec[i]
  X = sample(c(1,2), size=n, replace=T, prob=c(p,1-p))
  #eta=runif(n)
  eta=rbeta(n,1,1/2)
  for (j in 1:n){
    Y[j]=sample(c(1,2), size=1, replace=T, 
                prob=c(eta[j],1-eta[j])) 
  }
  res[,i]=(-3)*((X-Y)!=0)+2*((X==1)&(Y==1))
            +4*((X==2)&(Y==2))
}
boxplot(res, col="yellow",names=pvec)
grid()

install.packages("waveslim")
library(waveslim)
data(ibm)
plot(ibm)
X=diff(log(ibm))
plot(X)
f=function(p){
  -quantile(X,p)
}
plot(f, xlim=c(0,0.1))
g=function(p){
  -quantile(X,p,type=6)
}
xvec=seq(0,0.1,length=100)
lines(xvec, sapply(xvec,g),col="red")

Z=sort(X)
F0=function(x){
  if (Z[1]<=x){
    max(which(Z<=x))/n
  }
  else 0
}
r=floor(n*0.05)
F1=function(x){
  res=0
  for (k in r:n){
    res=res+choose(n,k)*(F0(x)**k)*((1-F0(x))**(n-k))
  }
  return(res)
}
xvec=seq(-0.05, 0.05, length=100)
plot(xvec,sapply(xvec, F1),type="l")


n=10000
M=1000
res=matrix(data=NA, ncol=2, nrow=M)
alpha=1
beta=1.5
for (i in 1:M){
  X=beta*(runif(n))**(1/alpha)
  res[i,1]=n/sum(log(max(X)/X))
  m1=mean(X)
  m2=mean(X**2)
  res[i,2]=-1+sqrt(m2/(m2-m1**2))
}
boxplot(res)

for (i in 1:M){
  X=beta*(runif(n))**(1/alpha)
  res[i,1]=max(X)
  m1=mean(X)
  m2=mean(X**2)
  alphahat=-1+sqrt(m2/(m2-m1**2))
  res[i,2]=m1*(1+1/alphahat)
}
boxplot(res[,1])

install.packages("stats4")
library(stats4)
?mle
alpha=1
beta=2
X=rbeta(1000, shape1=alpha, shape2=beta)
L=function(a,b){
  -sum(dbeta(X,a,b,log=TRUE))
}
mle(L ,start=list(a=0.5, b=1.5),method="L-BFGS-B",lower=c(0,0))

install.packages("gmm")
library(gmm)
?gmm
g=function(theta, u){
  a=theta[1]
  b=theta[2]
  m1=a/(a+b)-u
  m2=a*(a+1)/((a+b)*(a+b+1))-u^2
  return(cbind(m1,m2))
}
gmm(g,X,c(0.5,1.5))  

X=rnorm(1000, mean=15, sd=10)  
qqnorm(X)  
qqline(X, col="red")
