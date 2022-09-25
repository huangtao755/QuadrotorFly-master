function [next] = rk4(func, x0, u, h)
%RK4 �˴���ʾ�йش˺�����ժҪ
%   �˴���ʾ��ϸ˵��
    k1 = func(x0, u);
    k2 = func(x0' + h .* k1 ./ 2, u);
    k3 = func(x0' + h .* k2 ./ 2, u);
    k4 = func(x0' + h .* k3, u);
    next = x0' + h .* (k1 + 2 * k2 + 2 * k3 + k4) / 6;
end

