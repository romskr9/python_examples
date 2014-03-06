from math import *
import cmath

r = 1
c = 1
l = 1
g = 1

o = omega = 100

x = 0.5

def sqr(x):
	return x*x

beta = sqrt((r*g - sqr(o)*l*c + sqrt(sqr(r*g - sqr(o)*l*c) +sqr(o)*sqr(l*g + r*c))) / 2)

alpha = o*(l*g + r*c)/sqrt(2*(r*g - sqr(o)*l*c + sqrt(sqr(r*g - sqr(o)*l*c) +sqr(o)*sqr(l*g + r*c))))

print 'alpha = ', alpha, '\nbeta = ', beta

re = -sinh(2*beta)/(cos(2*alpha) + cosh(2*beta))

im = sin(2*beta)/(cos(2*alpha) + cosh(2*beta))

print 're = ', re, '\nim = ', im

re2 = sinh(2*beta)/(cosh(2*beta) - cos(2*alpha))
im2 = -sin(2*beta)/(cosh(2*beta) - cos(2*alpha))
print 're2 = ', re2, '\nim2 = ', im2

print 'x = ', x, ':'

ax = alpha*x
bx = beta*x

mcos = sin(ax)*sinh(bx) - cos(ax)*sinh(bx)*im - sin(ax)*cosh(bx)*re
msin = cos(ax)*cosh(bx) - cos(ax)*sinh(bx)*re + sin(ax)*cosh(bx)*im

mcos *=sqrt(2)
msin*=sqrt(2)
print 'mcos = ', mcos, '\nmsin = ', msin

x = 1
print 'x = ', x, ':'
ax = alpha*x
bx = beta*x

mcos = sin(ax)*sinh(bx) - cos(ax)*sinh(bx)*im - sin(ax)*cosh(bx)*re
msin = cos(ax)*cosh(bx) - cos(ax)*sinh(bx)*re + sin(ax)*cosh(bx)*im

mcos *=sqrt(2)
msin*=sqrt(2)
print 'mcos = ', mcos, '\nmsin = ', msin

gamma = beta+1j*alpha
zvi = 1/cmath.tanh(gamma)

print 'zvi', zvi