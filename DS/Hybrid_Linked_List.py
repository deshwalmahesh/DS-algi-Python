class Node:
    def __init__(self, data = None, next_pointer = None):
        self.data = data
        self.next_pointer = next_pointer

    def __str__(self):
        return self.__repr__()
    
    def __repr__(self):
        return str(self.data)


class LinkedList:
    def __init__(self):
        self.head = Node()
        self.length = 0

    def insert_node(self, data):
        new_node = Node(data) # node to be inserted
        current_node = self.head
        while current_node.next_pointer != None: # it'll only stop at the last node which is obviously empty
            current_node = current_node.next_pointer # bring out next pointer
        current_node.next_pointer = new_node

        self.length += 1


    def _handle_slices(self, slice_index):
        '''
        Handle the slicing operations
        '''
        index = slice_index.start if slice_index.start != None else 0
        stop = min(slice_index.stop, self.length -1) if slice_index.stop != None else self.length
        step = 1 if slice_index.step == None else slice_index.step
        if step < 1: raise ValueError("Reverse stepping not allowed")

        if index < 0: raise NotImplementedError("Negative slicing not implemented")

        if (index > self.length - 1) or (index < -self.length -1): raise ValueError(f"index {index} out of bounds of max length")
        if index < 0: index = self.length + index
        return index, stop, step


    def delete_node(self, index):
        if self.length == 0: raise ValueError(f"Can not delete from empty Linked List")
        if (index > self.length - 1) or (index < -self.length -1): raise ValueError(f"index {index} out of bounds of max length")
        if index < 0: index = self.length + index

        if index == 0:
            self.head.next_pointer = self[index].next_pointer if index != self.length -1 else None
        
        else: self[index-1].next_pointer = self[index].next_pointer if index != self.length -1 else None
        self.length -= 1
        

    def __getitem__(self, index):
        if isinstance(index, slice):
            return self._slice_return(index)
            
        if (index > self.length - 1) or (index < -self.length -1): raise ValueError(f"index {index} out of bounds of max length")
        if index < 0: index = self.length + index
        
        count = 0
        current_node = self.head.next_pointer
        while count != index:
            current_node = current_node.next_pointer
            count += 1
        
        return current_node

    
    def _slice_return(self, slice_index):
        '''
        Implement slicing Operation just like in Python Lists and Strings
        '''
        start, stop, step = self._handle_slices(slice_index)

        ll = LinkedList()
        for i in range(start, stop,step):
            ll.insert_node(self[i].data)
        return ll


    def __len__(self):
        return self.length
    

    def __str__(self):
        array = []
        node = self.head
        count = self.length
        while count > 0:
            node = node.next_pointer
            array.append(node.data)
            count -= 1
            
        return(str(array))


    def __repr__(self):
        return self.__str__()


    def __delitem__(self, index):
        '''
        Delete an item just like arrays and dict as" del object[index]
        '''
        if isinstance(index, slice):
            start, stop, step = self._handle_slices(index)
            if step > 1: raise ValueError("Logic of step > 1 is not working need a different approach")
            for _ in range(start,stop):
                self.delete_node(start)

        else: self.delete_node(index)

    
    def __iter__(self):
        '''
        Iterate over the data structure
        '''
        node = self.head
        while node.next_pointer != None:
            node = node.next_pointer
            yield node
