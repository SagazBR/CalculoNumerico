function [x] = jacobi(A,y,x0,TOL,N)
  //preliminares
  n = size(A,1)
  x = zeros(n,1)
  k = 1
  //iteracoes
  while (k <= N)
    //iteracao de Jacobi
    for i = 1:n
      x(i) = (y(i) - A(i,[1:i-1,i+1:n])*x0([1:i-1,i+1:n]))/A(i,i)
    end
    //depuracao
    disp([k,x',max(abs(x-x0))])
    //criterio de parada
    if (max(abs(x-x0))<TOL) then
      return x
    end
    //prepara nova iteracao
    x0 = x
    k = k+1
  end
  error('Num. max. de iteracoes!')
endfunction
