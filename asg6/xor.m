clc; close all; clear all;
P=[0 0 1 1; 0 1 0 1]; T=[0 1 1 0];
net= feedforwardnet(200);% 200-hidden layer
net.trainFcn = 'trainbr';
net.divideFcn = 'dividetrain';
[net, tr]= train(net,P,T);
Y = sim(net,P)
a=net(P(:,1));
a=net(P(:,2));
a=net(P(:,3));
a=net(P(:,4));
Y = sim(net,[1;0])
plotpv(P, T)
plotpc(net.iw{1,1},net.b{1})