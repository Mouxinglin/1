#coding:gbk
"""
��һ��С��Ŀ��Rock-paper-scissors-lizard-Spock
���ߣ�Ĳ����
���ڣ�2020.11.24
"""
import random

# 0 - ʯͷ
# 1 - ʷ����
# 2 - ֽ
# 3 - ����
# 4 - ����

# ����Ϊ�����Ϸ����Ҫ�õ����Զ��庯��

def name_to_number(name):
    if name=="ʯͷ":
        return 0
    elif name=="ʷ����":
        return 1
    elif name=="ֽ":
        return 2
    elif name=="����":
        return 3
    elif name=="����":
        return 4
    """
    ����Ϸ�����Ӧ����ͬ������
    """

    # ʹ��if/elif/else��佫����Ϸ�����Ӧ����ͬ������
    # ��Ҫ���Ƿ��ؽ��


    #��дִ�д���,������ɺ�passɾ��


def number_to_name(number):
    if number==0:
        return "ʯͷ"
    elif number==1:
        return "ʷ����"
    elif number==2:
        return "ֽ"
    elif number==3:
        return "����"
    elif number==4:
        return "����"
    """
    ������ (0, 1, 2, 3, or 4)��Ӧ����Ϸ�Ĳ�ͬ����
    """

    # ʹ��if/elif/else��佫��ͬ��������Ӧ����Ϸ�Ĳ�ͬ����
    # ��Ҫ���Ƿ��ؽ��

    #��дִ�д���,������ɺ�passɾ��


def rpsls(player_choice):
    a=random.randrange(0,4)
    player_choice=choice_name
    player_choice_number=name_to_number(player_choice)
    while player_choice_number==name_to_number('ʯͷ'):
        print('����ѡ��Ϊ��'+number_to_name(0)+','+'�������ѡ��Ϊ��'+number_to_name(a))
        if player_choice_number==a:
            print('���ͼ��������һ����')
        if a==3 or a==4:
            print('��Ӯ�ˣ�')
        if a==1 or a==2:
            print('�����Ӯ��')
        break
    while player_choice_number==name_to_number('ʷ����'):
        print('����ѡ��Ϊ��'+number_to_name(1)+','+'�������ѡ��Ϊ��'+number_to_name(a))
        if player_choice_number==a:
            print('���ͼ��������һ����')
        if a==4 or a==0:
            print('��Ӯ��')
        if a==2 or a==3:
            print('�����Ӯ��')
        break
    while player_choice_number==name_to_number('ֽ'):
        print('����ѡ��Ϊ��'+number_to_name(2)+','+'�������ѡ��Ϊ��'+number_to_name(a))
        if player_choice_number==a:
            print('���ͼ��������һ����')
        if a==1 or a==0:
            print('��Ӯ��')
        if a==3 or a==4:
            print('�����Ӯ��')
        break
    while player_choice_number==name_to_number('����'):
        print('����ѡ��Ϊ��'+number_to_name(3)+','+'�������ѡ��Ϊ��'+number_to_name(a))
        if player_choice_number==a:
            print('���ͼ��������һ����')
        if a==1 or a==2:
            print('��Ӯ��')
        if a==0 or a==4:
            print('�����Ӯ��')
        break
    """
    �û�����������һ��ѡ�񣬸���RPSLS��Ϸ��������Ļ�������Ӧ�Ľ��

    """


    # ���"-------- "���зָ�
    # ��ʾ�û�������ʾ���û�ͨ�����̽��Լ�����Ϸѡ��������룬�������player_choice

    # ����name_to_number()�������û�����Ϸѡ�����ת��Ϊ��Ӧ���������������player_choice_number

    # ����random.randrange()�Զ�����0-4֮��������������Ϊ��������ѡ�����Ϸ���󣬴������comp_number

    # ����number_to_name()����������������������ת��Ϊ��Ӧ����Ϸ����

    # ����Ļ����ʾ�����ѡ����������

    # ����if/elif/else ��䣬����RPSLS������û�ѡ��ͼ����ѡ������жϣ�������Ļ����ʾ�жϽ��

    # ����û��ͼ����ѡ��һ��������ʾ�����ͼ��������һ���ء�������û���ʤ������ʾ����Ӯ�ˡ�����֮����ʾ�������Ӯ�ˡ�

    #����������ʾ��дִ�д��룬������ɺ�ɾ����pass


# �Գ�����в���
print("��ӭʹ��RPSLS��Ϸ")
print("----------------")
print("����������ѡ��:")
choice_name=input()
if choice_name=='ʯͷ' or '����' or 'ֽ' or '����' or 'ʷ����':
   print(rpsls(choice_name))
else:
   print("Error: No Correct Name")
