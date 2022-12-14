class ListExercise:
    @staticmethod
    def replace(input_list: list[int]) -> list[int]:
        new_list = []
        max_list = 0
        i = 0
        for element in input_list:
            if element > max_list:
                max_list = element
        for element in input_list:
            i += 1
            if element > 0:
                new_list.insert(i, max_list)
            else:
                new_list.insert(i, element)
        return new_list
        pass

    @staticmethod
    def search(input_list: list[int], query: int) -> int:
        def recursion(start, end):
            if start > end:
                return -1
            mid = (start + end) // 2
            if query == input_list[mid]:
                return mid
            if query < input_list[mid]:
                return recursion(start, mid - 1)
            else:
                return recursion(mid + 1, end)

        return recursion(0, len(input_list) - 1)
        pass
