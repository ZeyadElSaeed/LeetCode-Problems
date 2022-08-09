class MyStack {
    Queue<Integer> main;
    Queue<Integer> help;
    public MyStack() {
        main= new LinkedList<Integer>();
        help= new LinkedList<Integer>();
    }
    
    public void push(int x) {
        main.add( x ); 
    }
    
    public int pop() {
        if ( main.size() == 0 ) return -1;
        while ( main.size() > 1 )
            help.add( main.remove() );
        int x = main.remove();
        while ( !help.isEmpty() )
            main.add( help.remove() );
        return x;
        
    }
    
    public int top() {
        if ( main.size() == 0 ) return -1;
        while ( main.size() > 1 )
            help.add( main.remove() );
        int x = main.peek();
        help.add( main.remove() );
        while ( !help.isEmpty() )
            main.add( help.remove() );
        return x;
        
    }
    
    public boolean empty() {
        return main.isEmpty();
        
    }
}

/**
 * Your MyStack object will be instantiated and called as such:
 * MyStack obj = new MyStack();
 * obj.push(x);
 * int param_2 = obj.pop();
 * int param_3 = obj.top();
 * boolean param_4 = obj.empty();
 */