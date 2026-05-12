import re

def smart_chunking(text_string: str, max_chars: int = 500):
    # 1. Normalización: Convertimos saltos de línea extraños en saltos estándar
    # y detectamos párrafos incluso si solo tienen un salto pero van seguidos de una mayúscula
    # (Esto es útil si el texto viene "sucio")
    text_string = text_string.replace('\r\n', '\n')
    
    # 2. Dividimos por cualquier secuencia de uno o más saltos de línea
    # que estén rodeados de espacios en blanco.
    raw_paragraphs = re.split(r'\n+', text_string)
    
    chunks = []
    current_batch = ""

    for p in raw_paragraphs:
        p = p.strip()
        if not p: continue

        # Calculamos el tamaño si añadiéramos este párrafo
        # Sumamos 2 por los saltos de línea que pondremos entre párrafos
        potential_length = len(current_batch) + len(p) + 2 if current_batch else len(p)

        if potential_length <= max_chars:
            if current_batch:
                current_batch += "\n\n" + p
            else:
                current_batch = p
        else:
            # Si añadirlo supera el límite, guardamos lo que tenemos y empezamos uno nuevo
            if current_batch:
                chunks.append(current_batch)
            current_batch = p

    # Añadimos el último bloque
    if current_batch:
        chunks.append(current_batch)

    return chunks