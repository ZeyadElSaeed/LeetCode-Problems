class MyQueue {
    private Stack<Integer> main ;
    private Stack<Integer> help ;
    
    public MyQueue() {
        main = new Stack<Integer>();
        help = new Stack<Integer>(); 
    }
    
    public void push(int x) {
        main.push(x);
    }
    
    public int pop() {
        if ( main.empty() ) return -1;
        while ( !main.empty() )
            help.push( main.pop() );
        int x = help.pop();
        while ( !help.empty() )
            main.push( help.pop() );
        return x;
        
    }
    
    public int peek() {
        if ( main.empty() ) return -1;
        while ( !main.empty() )
            help.push( main.pop() );
        int x = help.peek();
        while ( !help.empty() )
            main.push( help.pop() );
        return x;
        
    }
    
    public boolean empty() {
        return main.empty() ;
        
    }
}

/**
 * Your MyQueue object will be instantiated and called as such:
 * MyQueue obj = new MyQueue();
 * obj.push(x);
 * int param_2 = obj.pop();
 * int param_3 = obj.peek();
 * boolean param_4 = obj.empty();
 */