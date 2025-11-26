# # import re

# # padrao_num_conta = re.compile(r'\d{8}-\d{2}')
# # x = input('Coloque o numero da contya: ')
# # valido = padrao_num_conta.findall(x)
# # if valido:
# #     print('válido')
# # else:
# #     print('inválido')
# # print(valido)

# # from pprint import pprint
# # data = [
# #     {"id":1, "nome": "Maria", "salario": 4500.03},
# #     {"id":2, "nome": "José", "salario": 6500.05},
# #     {"id":3, "nome": "Antonio", "salario": 3409.98},
# #     {"id":4, "nome": "Ana", "salario": 5093.34},
# #     {"id":5, "nome": "Mariana", "salario": 3458.54},
# #     {"id":6, "nome": "Ana", "salario": 10932.59},
# # ]
# # pprint(data)

# import this


# class Solution:
#     def addTwoNumbers(self, l1: list, l2:list) :
#         result1 = 0
#         result2 = 0

#         for num in l1:
#             result1 = result1 * 10 + num
        
#         for num in l2:
#             result2 = result2 * 10 + num
        
#         result = str(result1 + result2)
#         result = result[::-1]
#         end_result = []

#         for num in result:
#             end_result.append(int(num))
        

#         return end_result
        
        
# # l1 = [2, 4, 3]
# # l2 = [5, 6, 4]
# # l1 = [0]
# # l2 = [0]
# l1 = [9,9,9,9,9,9,9]
# l2 = [9,9,9,9]
# solution = Solution()
# print(solution.addTwoNumbers(l1,l2))
  # --- 1. Definição da Estrutura de Dados (ListNode) ---
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# --- 2. A Solução do Problema ---
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        dummy_head = ListNode(0)
        current = dummy_head
        carry = 0
        
        # Use 'is not None' ou o próprio objeto em condições Pythônicas
        while l1 or l2 or carry:
            
            val1 = l1.val if l1 else 0
            val2 = l2.val if l2 else 0
            
            total_sum = val1 + val2 + carry
            carry = total_sum // 10
            digit = total_sum % 10
            
            current.next = ListNode(digit)
            current = current.next
            
            # Avança os ponteiros
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None
            
        return dummy_head.next

# --- 3. Funções Auxiliares para Teste Local (Prática Profissional) ---

def create_linked_list(arr):
    """Cria uma ListNode a partir de uma lista Python."""
    if not arr:
        return None
    head = ListNode(arr[0])
    current = head
    for val in arr[1:]:
        current.next = ListNode(val)
        current = current.next
    return head

def print_linked_list(head):
    """Imprime os valores de uma ListNode."""
    arr = []
    current = head
    while current:
        arr.append(current.val)
        current = current.next
    return arr # Retorna a lista como array

# --- 4. Testes (Exemplo 1: 342 + 465 = 807) ---
l1_arr = [2, 4, 3] # Representa 342
l2_arr = [5, 6, 4] # Representa 465

l1 = create_linked_list(l1_arr)
l2 = create_linked_list(l2_arr)

solution = Solution()
resultado_linked_list = solution.addTwoNumbers(l1, l2)

# Imprime o resultado formatado
print(f"L1 (Lista Encadeada): {print_linked_list(l1)}")
print(f"L2 (Lista Encadeada): {print_linked_list(l2)}")
print(f"Resultado (Ordem Inversa): {print_linked_list(resultado_linked_list)}")
# Resultado esperado: [7, 0, 8]