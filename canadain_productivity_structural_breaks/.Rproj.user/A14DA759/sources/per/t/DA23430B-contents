library(gets)
library(fastDummies)
library(magrittr)

data <- read.csv('../canadain_oil_mining_gdp_productivity.csv')

plot(as.Date(data$REF_DATE),data$VALUE,type = "l")

T <- NROW(data$VALUE)

t <- as.vector(seq(1:T))
y <- as.vector(data$VALUE) #dependent variable y = mx + b + error

#create dummies
quarters = dummy_cols(data$quarter)

q1 <- sim(T)*quarters[,2]
q2 <- sim(T)*quarters[,3]
q3 <- sim(T)*quarters[,4]
q4 <- sim(T)*quarters[,5]

Q <- cbind(q1,q2,q3,q4)

p_alpha <- 1/(NCOL(Q)+T+(T-1))

dy <- diff(y, 1)

out <- isat(y, mxreg=t, ar=1, uis=Q, iis=TRUE, sis=TRUE, tis = FALSE, plot=TRUE, t.pval=p_alpha)

#dates <- mining_data %>% dplyr::slice(1:109)
plot(fitted(out),type = "l",col = "red")
lines(y)

isat(y, mxreg=t, ar=1, uis=Q, iis=TRUE, sis=TRUE, tis = FALSE, plot=TRUE, t.pval=p_alpha)



