p = [0 1];
t = [1 0];
net = perceptron;
net = train(net, p, t);
net.trainParam.epochs = 20;
Y = sim(net,[0])
Y = sim(net,p);
plotpv(p,Y)