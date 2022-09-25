function rateDot = dynamic_actuator(rotorRate, u)
%DYNAMIC_ACTUATOR �˴���ʾ�йش˺�����ժҪ
%   �˴���ʾ��ϸ˵��
    rotor_t=1.36e-2;
    rotor_cr=646;
    rotor_wb=166;
    rateDot = 1 / rotor_t * (rotor_cr * u + rotor_wb - rotorRate);
end

