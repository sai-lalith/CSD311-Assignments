input = [0 0; 1 1];
numIn = 4;
desired_out = [1;0];
bias = -1;
coeff = 0.7;
rand('state',sum(100*clock));
weights = -1*2.*rand(3,1);

for i = 1:iterations
     out = zeros(4,1);
     for j = 1:numIn
          y = bias*weights(1,1)+ input(j,1)*weights(2,1)+input(j,2)*weights(3,1);
          out(j) = 1/(1+exp(-y));
          delta = desired_out(j)-out(j);
          weights(1,1) = weights(1,1)+coeff*bias*delta;
          weights(2,1) = weights(2,1)+coeff*input(j,1)*delta;
          weights(3,1) = weights(3,1)+coeff*input(j,2)*delta;
     end
end
out 
weights