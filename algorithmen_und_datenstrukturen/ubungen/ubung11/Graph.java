import java.util.*;
import Bag.java;

public class Graph {
    private final int V;
    private int E;
    private Bag<Integer>[] adjacencyList;

    public Graph(int V) {
        this.V = V; 
        this.E = 0;
        adjacencyList = (Bag<Integer>[]) new Bag[V];
        for (int v = 0; v < V; v++) {
            adjacencyList[v] = new Bag<Integer>();
        }
    }

    public Graph(In in) {
        this(in.readInt());
        int E = in.readInt();
        for(int i = 0; i < E; i++) {
            int v = in.readInt();
            int w = in.readInt();
            addEdge(v, w);
        }
    }

    public int V() {return V;}
    public int E() {return E;}

    public void addEdge(int v, int w){
        adjacencyList[v].add(w);
        adjacencyList[w].add(v);
        E++;
    }

    public Iterable<Integer> adj(int v){
        return adjacencyList[v];
    }
}