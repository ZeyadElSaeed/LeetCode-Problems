class MinStack {
    private List<Integer> data;
    int minIndex;
    public MinStack() {
        data = new ArrayList<Integer>();
    }
    
    public void push(int val) {
        if ( data.isEmpty() ){
            minIndex = 0;
            data.add(val);
        }
        else {
            data.add(val);
            minIndex = data.get( data.size() -1)<data.get( minIndex )? data.size() -1 : minIndex;
        }
        
    }
    
    public void pop() {
        if (data.isEmpty()) return ;
        if ( minIndex == data.size() - 1){
            data.remove( data.size() -1);
            minIndex = data.size() -1;
            for ( int i=0; i<data.size()-1; i++)
                minIndex = data.get( i ) < data.get( minIndex )? i : minIndex;
        }
        else {
            data.remove ( data.size() -1);
        }
    }
    
    public int top() {
        if (data.isEmpty()) return -1;
        return data.get( data.size() -1);
    }
    
    public int getMin() {
        if (data.isEmpty()) return -1;
        return data.get( minIndex );
    }
}

/**
 * Your MinStack object will be instantiated and called as such:
 * MinStack obj = new MinStack();
 * obj.push(val);
 * obj.pop();
 * int param_3 = obj.top();
 * int param_4 = obj.getMin();
 */