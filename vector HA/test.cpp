#include <vector>
#include<iostream>
#include<algorithm>
#include<numeric>
#include<string>
//Implement a function that takes a vector of integers and returns the sum of all the elements in the vector.
int sum(const std::vector<int> &temp){
  return std::accumulate(temp.begin(),temp.end(),0.00);
}
std::vector<std::string> sort_words ( std::vector<std::string> &temp){
  std::sort(temp.begin(),)
}
int main() {
  std::vector<int> res {1,2,3,4,5,6,7,8,9};
  std::cout << sum(res);

Position task1(const Vector<NBA_Player>& v){
  	if(v.empty()) throw std::runtime_error("Error with task1");
    std::unordered_map<Position,size_t> positions_counts;
  	std::for_each(v.begin(),v.end(),[&](const NBA_Player & player){
    	++positions_counts[player.get_position()];
    });
		auto max_position = std::max_element(positions_counts.begin(),positions_counts.end(),[](const auto & player1,const auto & player2){
    	return player1.second < player2.second;
    });
  	Position res = max_position->first;
  	std::for_each(positions_counts.begin(),positions_counts.end(),[&](const auto & element){
    	if(element.second == max_position->second && element.first <= res ){
      	res = element.first;
        
      }
    });
  	
  	return res;
                                                                             
	
  }
  vector<NBA_Player> task2(const Vector<NBA_Player>& v){
    Vector<NBA_Player> vec(v.size());
    std::transform(v.begin(),v.end(),vec.begin(),[vec](const NBA_Player & player )
    {
      std::string big_name = player.get_name();
      std::transform(big_name.begin(),big_name.end(),big_name.begin(),[](char c)
      {
        return std::toupper(c); 
      });
      return NBA_Player temp_obj(temp_name,elem.get_team(),elem.get_position(),elem.get_height(),elem.get_stats());
    });
    return vec;
    }

    vector<NBA_Player> task2(const Vector<NBA_Player>& v){
  	vector<NBA_Player> res(v.size());
		std::transform(v.begin(),v.end(),res.begin(),[](const NBA_Player & elem)
    {   
        
      	std::string temp_name = elem.get_name();
      	
        std::transform(temp_name.begin(),temp_name.end(),temp_name.begin(),[](char c)
        {   
            if(c >=97) return std::toupper(c);
        });
      NBA_Player temp_obj(temp_name,elem.get_team(),elem.get_position(),elem.get_height(),elem.get_stats());
      	
		return 		temp_obj;
    });
  	return res;
    }
    template<>
    Vector<NBA_Player>::IteratorB & Vector<NBA_Player>::IteratorB::operator++()

  return 0;
}