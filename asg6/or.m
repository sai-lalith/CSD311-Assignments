x = [0 1 0 1; 0 0 1 1];
t = [0 1 1 1];
net = perceptron;
net = configure(net,x,t);
net.iw{1,1} = [0.5,0.5];
net.b{1} = [0.2];
net.trainParam.epochs = 20;
net = train(net,x,t);
Z = sim(net,x)
plotpv(x, Z)
plotpc(net.iw{1,1},net.b{1})