class Solution {
    public boolean canVisitAllRooms(List<List<Integer>> rooms) {
        Queue<Integer> q = new LinkedList<Integer>();
        int n = rooms.size();
        boolean[] visited = new boolean[n];
        visited[0] = true;
        for(int i =0; i<rooms.get(0).size(); i++)
            q.add( rooms.get(0).get(i) );
        while ( !q.isEmpty() ){
            int room = q.remove();
            visited[room] = true;
            for(int i =0; i<rooms.get(room).size(); i++)
                if ( !visited[rooms.get(room).get(i)] )
                    q.add( rooms.get(room).get(i) );
        }
        for(int i =0; i<n; i++)
            if(!visited[i])
                return false;
        return true;
        
        
    }
}