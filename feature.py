from  import
def extract_features(question):
    features = {
        # Độ dài và cấu trúc
        "length": len(question.split()),
        "avg_word_length": average_word_length(question),
        
        # Độ phức tạp từ vựng
        "rare_words": count_rare_words(question),
        "subject_terms": count_domain_terms(question),
        
        # Cấu trúc ngữ pháp
        "clause_count": count_clauses(question),
        "syntax_depth": parse_tree_depth(question)
    }
    return features